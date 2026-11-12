import os
from google import genai
from google.genai import types
from pathlib import Path


# Locate the project root independently of the working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_documents():
    """Load Markdown documents and extract their metadata."""

    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw data directory not found: {RAW_DATA_DIR}"
        )

    document_files = sorted(RAW_DATA_DIR.rglob("*.md"))

    if not document_files:
        raise FileNotFoundError(
            f"No Markdown documents found in {RAW_DATA_DIR}"
        )

    documents = []

    for file_path in document_files:

        raw_text = file_path.read_text(encoding="utf-8")

        # Separate YAML-style metadata from the document content.
        parts = raw_text.split("---", maxsplit=2)

        if len(parts) != 3 or parts[0].strip():
            raise ValueError(
                f"Missing metadata section in {file_path.name}"
            )

        metadata_text = parts[1]
        content = parts[2].strip()

        # Read the simple key-value metadata fields.
        metadata = {}

        for line in metadata_text.splitlines():
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                raise ValueError(
                    f"Invalid metadata line in {file_path.name}: {line}"
                )

            key, value = line.split(":", maxsplit=1)

            metadata[key.strip()] = value.strip().strip('"').strip("'")

        if not content:
            raise ValueError(
                f"No document content found in {file_path.name}"
            )

        metadata["source_file"] = str(
            file_path.relative_to(PROJECT_ROOT)
        )

        documents.append({
            "content": content,
            "metadata": metadata
        })

    return documents

def split_into_chunks(documents, chunk_size=150, overlap=30):
    """Split documents into overlapping word-based chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size.")

    chunks = []

    for document in documents:
        words = document["content"].split()

        start = 0
        chunk_index = 0

        while start < len(words):
            end = min(start + chunk_size, len(words))

            chunk_text = " ".join(words[start:end])

            # Preserve the original document metadata.
            chunk_metadata = document["metadata"].copy()
            chunk_metadata["chunk_index"] = chunk_index

            chunks.append({
                "content": chunk_text,
                "metadata": chunk_metadata
            })

            chunk_index += 1

            if end == len(words):
                break

            start = end - overlap

    return chunks

EMBEDDING_MODEL = "gemini-embedding-001"
EMBEDDING_DIMENSION = 768


def generate_document_embeddings(chunks):
    """Generate embeddings for document chunks."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set.")

    if not chunks:
        return []

    client = genai.Client(api_key=api_key)

    texts = [chunk["content"] for chunk in chunks]

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=texts,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=EMBEDDING_DIMENSION
        )
    )

    if not response.embeddings or len(response.embeddings) != len(chunks):
        raise RuntimeError("The embedding response does not match the input chunks.")

    embeddings = [
        embedding.values
        for embedding in response.embeddings
    ]

    return embeddings
