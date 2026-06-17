from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Conversation RAG System API", "status": "online"}

@app.get("/persona")
def persona():
    return {"habits": {"sleep": "Late sleeper", "food": "Coffee drinker"}, "personality": ["Humorous", "Optimistic"]}

@app.get("/health")
def health():
    return {"ok": True}
