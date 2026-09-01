from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ai_answer
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.post("/chat")
def chat(req: ChatRequest):

    print("收到问题：", req.question)

    answer = ai_answer(req.question)

    print("AI返回：", answer)

    return {
        "answer": answer
    }