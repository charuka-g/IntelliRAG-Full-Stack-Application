from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.rag import get_answer_and_docs
from src.qdrant import upload_website_to_collection
from fastapi.middleware.cors import CORSMiddleware

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    message: str

app = FastAPI(
    title="RAG API",
    description="API for RAG",
    version="0.1"
)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
)

@app.post("/chat", description="Chat with the model from this endpoint")
def chat(request: ChatRequest):
    # Use the message from the request body
    response = get_answer_and_docs(request.message)
    response_content = {
        "question": request.message,
        "answer": response["answer"],
        "documents": [doc.dict() for doc in response["context"]]
    }
    return JSONResponse(content=response_content, status_code=200)


@app.post("/Indexing", description="Indexing a websitthrough this endpoint")
def indexing(url: str):
    try:
        response = upload_website_to_collection(url)
        return JSONResponse(content={"response": response}, status_code=200)   
     
    except Exception as e:
        return JSONResponse(content={"response": str(e)}, status_code=400)
    



