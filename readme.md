Objective
- make a search engine that can take any string from any main language and reply considering synonyms and context

Actions
- use llm provided, ollama local,  embeddings for each entry in the db, store locally and run before app is served
- use streamlit as frontend
- get embedding from prompt
- compare with Euclidean distance
- present to user sorted by proximity

Architectural options
- https://www.youtube.com/watch?v=8L3tGcYc774
- https://medium.com/@devbytes/similarity-search-with-faiss-a-practical-guide-to-efficient-indexing-and-retrieval-e99dd0e55e8c
