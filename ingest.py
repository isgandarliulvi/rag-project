from src.utils import load_azure_configs
from src.rag_pipeline import load_document, split_documents_into_chunks, create_and_store_embeddings


DATA_PATH = "data/sample_document.pdf"  # Path to the document to be processed
VECTOR_STORE_PATH = "vector_store"      # Directory to save the vector database

def main():

    # 1. Load the API key
    azure_config = load_azure_configs()

    # 2. Load the document
    documents = load_document(DATA_PATH)
    
    # 3. Split the documents into chunks
    chunks = split_documents_into_chunks(documents)
    
    # 4. Create embeddings and store them in the vector database
    create_and_store_embeddings(chunks, VECTOR_STORE_PATH, azure_config)


if __name__ == "__main__":
    main()

    

