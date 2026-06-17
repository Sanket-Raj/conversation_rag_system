from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Conversation RAG System API Online"}

@app.get("/persona")
def get_persona():
    return {
        "habits": {
            "sleep_patterns": "Late sleeper",
            "food_habits": "Coffee drinker",
            "work_patterns": "Career-focused"
        }
    }
