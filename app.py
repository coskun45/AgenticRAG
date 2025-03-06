from dotenv import load_dotenv
from graph.graph import app
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load environment variables from the .env file
load_dotenv()

# Create the FastAPI app
app_fastapi = FastAPI()

# Define a Pydantic model for the request body
class QuestionRequest(BaseModel):
    question: str

# Main endpoint that accepts POST requests
@app_fastapi.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question  # Extract the question from the request

    # If no question is provided, return a 400 error
    if not question:
        raise HTTPException(status_code=400, detail="No question provided")

    try:
        # Invoke the app function with the provided question
        response = app.invoke(input={"question": question})
        
        # Return the response as a JSON object
        return {"response": response}
    except Exception as e:
        # If any error occurs, raise a 500 error with the exception message
        raise HTTPException(status_code=500, detail=str(e))

# The FastAPI app will be run with Uvicorn, typically from the terminal with the following command:
