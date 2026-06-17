# Conversation RAG System with Persona Extraction

A system that processes conversations chronologically, detects topic changes, extracts user persona, and provides a chatbot interface for querying.

## How Topic Changes are Detected

Messages are scanned chronologically using keyword matching. Each message's text is analyzed against predefined topic keywords (work, food, health, entertainment, personal). When the dominant topic shifts from the previous message cluster, a new topic checkpoint is created with a summary of that segment. This ensures context boundaries align with actual topic shifts rather than arbitrary message counts.

## How Retrieval Works

When a user queries the system, the query is converted into a lightweight embedding representation. This embedding is compared against all stored checkpoint embeddings using cosine similarity scoring. The top matching topic summaries and message chunks are retrieved and combined to generate contextual answers. The system uses lightweight embeddings (no heavy transformer models) for fast, efficient retrieval without external API calls.

## How Persona is Built

The system scans all conversation messages for behavioral signals:

- **Habits**: Extracted from message timestamps (sleep patterns), food/drink keywords (food habits), work mentions (work patterns)
- **Personal Facts**: Relationships, life events, employment status derived from explicit mentions
- **Personality Traits**: Sentiment analysis for optimism, frequency of humor/sarcasm markers, emotional tone
- **Communication Style**: Average message length, emoji frequency, formality level, use of abbreviations

All signals are stored in a structured JSON with confidence levels, creating an honest persona representation based on actual conversation patterns.

## Project Structure
conversation_rag_system/
├── data/
│   ├── conversations.csv
│   ├── processed_checkpoints.json (auto-generated)
│   └── user_persona.json (auto-generated)
├── src/
│   ├── data_processor.py
│   ├── topic_detector.py
│   ├── rag_system.py
│   ├── persona_extractor.py
│   ├── chatbot.py
│   └── embeddings.py
├── main.py
└── requirements.txt
