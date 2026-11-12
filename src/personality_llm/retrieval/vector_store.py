
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
