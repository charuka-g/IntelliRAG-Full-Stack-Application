# import os
# # Optionally set the USER_AGENT at the start of your script
# os.environ["USER_AGENT"] = "MyApp/1.0 (contact@example.com)"

from decouple import config
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import WebBaseLoader

# # Updated import for the non-deprecated Qdrant vector store class
# from langchain_qdrant import QdrantVectorStore

# from qdrant_client import QdrantClient, models

# # Load configuration variables
# qdrant_api_key = config("QDRANT_API_KEY")
# print(qdrant_api_key)
qdrant_url = config("QDRANT_URL")
# print(qdrant_url)
# collection_name = "Websites"

# # Initialize the Qdrant client, optionally increase timeout if needed
# client = QdrantClient(
#     url=qdrant_url,
#     api_key=qdrant_api_key,
#     # timeout=30  # Increase the timeout (adjust as needed)
# )
# print("Check point 01")
# # Initialize the HuggingFace embeddings model
# # huggingface_embeddings = HuggingFaceEmbeddings(
#     # model_name="sentence-transformers/all-MiniLM-L6-v2"
# # )

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
# print("Check point 02")

# # Initialize the vector store using the updated class
# vector_store = QdrantVectorStore(
#     client=client,
#     collection_name=collection_name,
#     embedding=embeddings
# )
# print("Check point 04")

# # Initialize the text splitter
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=20,
#     length_function=len
# )
# print("Check point 05")

# def create_collection(collection_name: str):
#     """
#     Creates a new Qdrant collection with the appropriate vector size.
#     For the HuggingFace model "all-MiniLM-L6-v2", the embedding size is 384.
#     """
#     client.create_collection(
#         collection_name=collection_name,
#         vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
#     )
#     print(f"Collection '{collection_name}' created successfully.")
# print("Check point 03")

# def upload_website_to_collection(url: str):
#     """
#     Loads a webpage, splits its content into chunks, and uploads them
#     into the Qdrant collection. Each document's metadata contains the source URL.
#     """
#     # Check if the collection exists; if not, create it
#     if not client.collection_exists(collection_name=collection_name):
#         create_collection(collection_name)
        
#     # Load and split the webpage content
#     loader = WebBaseLoader(url)
#     docs = loader.load_and_split(text_splitter)
    
#     # Annotate each document with its source URL
#     for doc in docs:
#         doc.metadata = {"source_url": url}
    
#     # Add the documents to the vector store
#     vector_store.add_documents(docs)
#     return f"Successfully uploaded {len(docs)} documents to collection '{collection_name}' from {url}"

# # Optionally create the collection in advance (upload_website_to_collection handles this check)
# create_collection(collection_name)
# print("Check point 06")

# # Upload a sample website to the collection
# upload_website_to_collection("https://hamel.dev/blog/posts/evals/")
# print("Check point 07")

import httpx

try:
    response = httpx.get(qdrant_url, timeout=10)
    print("Response status:", response.status_code)
except Exception as e:
    print("Error during simple HTTPS request:", e)