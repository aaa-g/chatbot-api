from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def index():
    return JSONResponse({"message": "Welcome to Chatbot API! Use POST /api/chatbot"})
