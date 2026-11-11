# LLM_Research_Personality_tests

## Project Overview

My project investigates how different LLM architectures perform when combining information from multiple personality and typing frameworks to generate personalized study recommendations.

The user already knows their results from the assessments they have completed and provides them to the LLM. The system does not attempt to predict the user's personality based on textual data. Instead, it retrieves information about the selected types and traits from a structured knowledge base.

For example, a user can provide their MBTI type, Big Five scores and Enneagram type, and ask:

"What would be the most suitable way for me to study?"

The LLM retrieves the relevant characteristics, strengths, weaknesses and other information associated with these results and uses them to formulate a recommendation.

## Personality and Typing Frameworks

The planned knowledge base includes:

- **MBTI:** 16 personality types and their cognitive functions.
- **Big Five / BFAS:** Five major traits and ten personality aspects.
- **Enneagram:** Nine types, core fears, motivations and wings.
- **Human Design:** Types, strategies, authorities, profiles and centres.
- **16-season Color Analysis:** Seasonal categories, undertones, value and chroma.

The source documents will be collected and processed separately for each framework. This allows me to add or replace sources without changing the entire retrieval pipeline.

## Experimental Methodology

I compare four experimental setups:

1. Baseline LLM without external retrieval.
2. Standard Vector RAG using embeddings and a local vector database.
3. Advanced RAG Optimization using metadata tagging and reranking.
4. Knowledge Graph Traversal for retrieving interconnected information across multiple frameworks.

## Initial Proof of Concept

I first start with MBTI and Enneagram descriptions. I use these two frameworks to implement document processing and a standard vector-based RAG pipeline before extending the knowledge base.

## Project Structure

- `data/raw/` – Original source documents, separated by framework.
- `data/processed/` – Cleaned and processed documents.
- `src/personality_rag/data_processing/` – Document loading, cleaning and chunking.
- `src/personality_rag/retrieval/` – Embeddings and retrieval.
- `src/personality_rag/experiments/` – Experimental implementations.
- `tests/` – Tests for the implementation.
- `docs/` – Project documentation and data sources.

## Development Environment

The project is implemented in Python using Visual Studio Code.

## Evaluation

I evaluate the different approaches using:

- Retrieval Precision and Recall.
- Hallucination Reduction Rate.
- Synthesis Accuracy.
- Computational Efficiency (token consumption and response latency).