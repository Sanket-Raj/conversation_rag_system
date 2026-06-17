from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_processor import DataProcessor
from src.topic_detector import TopicDetector
from src.rag_system import RAGSystem
from src.persona_extractor import PersonaExtractor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

processor = DataProcessor("data/conversations.csv")
messages = processor.load_and_process()
detector = TopicDetector()
topic_segments = detector.detect_topics(messages)
rag = RAGSystem()
rag.build(messages, topic_segments)
extractor = PersonaExtractor()
persona = extractor.extract(messages)

@app.get("/")
def root():
    return {"message": "Conversation RAG System API"}

@app.get("/persona")
def get_persona():
    return persona

@app.get("/query")
def query(q: str):
    if "person" in q.lower():
        return {"answer": str(persona)}
    elif "habit" in q.lower():
        return {"answer": str(persona.get("habits", {}))}
    elif "communicate" in q.lower():
        return {"answer": str(persona.get("communication_style", {}))}
    else:
        return {"answer": rag.query(q)}

@app.get("/checkpoints")
def get_checkpoints():
    return {"checkpoints": rag.checkpoints}
