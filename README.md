# IntelliRAG

## Overview
**IntelliRAG** is a full-stack Retrieval-Augmented Generation (RAG) application designed to provide intelligent answers based on contextual information retrieved from indexed web sources. The system integrates OpenAI's GPT model, Qdrant for vector search, and a FastAPI backend, coupled with a React-based frontend.

## Features
- **Web-based Question Answering**: Users can input questions, and the system retrieves relevant documents before generating a response.
- **Automated Website Indexing**: The application allows users to index web pages to enhance retrieval quality.
- **Vector-Based Search**: Utilizes Qdrant as a vector store for efficient document retrieval.
- **FastAPI Backend**: Handles API requests for chat interactions and indexing.
- **React Frontend**: Provides a seamless UI for user interaction.

## Architecture
The project is built using a microservices-inspired structure:
- **Backend (FastAPI)**:
  - Handles user queries and document indexing.
  - Uses Qdrant for vector-based search.
  - Connects to OpenAI’s GPT model for generating responses.
- **Frontend (React.js)**:
  - Provides a web interface for users to interact with the RAG system.
  - Sends queries and indexing requests to the backend.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Node.js 16+
- Qdrant (Cloud or Local Deployment)
- OpenAI API Key

### Backend Setup
```sh
# Clone the repository
git clone https://github.com/your-repo/intellirag.git
cd intellirag

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export QDRANT_API_KEY="your_qdrant_api_key"
export QDRANT_URL="your_qdrant_instance_url"
export OPENAI_API_KEY="your_openai_api_key"

# Run FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Setup
```sh
cd frontend
npm install
npm start
```

## Usage
1. Navigate to `http://localhost:3000/`.
2. Ask questions through the UI.
3. Use the "Index" button to add website content to the database.
4. Retrieve enhanced responses using the indexed content.

## API Endpoints
### Chat Endpoint
**POST /chat**
```json
{
  "message": "What is artificial intelligence?"
}
```
**Response:**
```json
{
  "question": "What is artificial intelligence?",
  "answer": "AI is a branch of computer science...",
  "documents": [
    {"source_url": "https://example.com"}
  ]
}
```

### Indexing Endpoint
**POST /Indexing**
```json
{
  "url": "https://example.com"
}
```
**Response:**
```json
{
  "response": "Successfully uploaded documents from example.com"
}
```

## Future Enhancements
- Real-time streaming responses.
- Authentication & user roles.
- Support for multiple retrieval backends.

## License
This project is licensed under the MIT License.

## Contributors
- Your Name (Lead Developer)
- Other Contributors

