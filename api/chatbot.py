from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/chatbot")
async def chatbot_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
  
    ai_response = f"You said: {user_message}. AI replies: Hello there!"
    
    return JSONResponse({"response": ai_response})
