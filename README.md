# LLM Research: Personality Tests

This project explores how different large language model approaches can use personality framework information to answer questions based on a user's personality assessment results.

The initial version focuses on MBTI and Enneagram. The user provides their own assessment results, and the LLM uses information about those frameworks to generate personalized answers. The goal is not to predict someone's personality from their writing.

I want to compare different approaches and investigate whether providing the model with a structured knowledge base improves the relevance and accuracy of its answers.

The project will compare four approaches:

- **Baseline:** The LLM receives the user's profile and question directly, without retrieving external information.
- **Vector RAG:** The LLM retrieves relevant information from a vector database before generating an answer.
- **Advanced RAG:** The retrieval process is optimized using techniques such as metadata filtering and reranking.
- **Graph RAG:** The LLM uses relationships between concepts in a knowledge graph to retrieve supporting information.

The first implementation will be the baseline. The other approaches will be added afterwards so their results can be compared using the same questions and user profiles.