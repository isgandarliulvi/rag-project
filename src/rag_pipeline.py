from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings,  AzureChatOpenAI
from langchain_community.vectorstores import Chroma 
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough


def load_document(file_path):
    """Loads a PDF document from the specified file path."""

    print(f"Loading document: {file_path}")
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def split_documents_into_chunks(documents):
    """Splits documents into smaller chunks."""

    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    print(f"Total {len(chunks)} chunks created.")
    return chunks


def create_and_store_embeddings(chunks, persist_directory, azure_configs):
    """
    Creates embeddings from chunks and stores them in ChromaDB.
    """
    print("Generating embeddings and saving to the database...")

    # Azure OpenAI Embeddings setup
    embedding_config = azure_configs["embedding"]
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=embedding_config["deployment"],
        azure_endpoint=embedding_config["endpoint"],
        api_key=embedding_config["api_key"],
        api_version=embedding_config["api_version"],
    )
    
    # Create Chroma vector store
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print(f"Database successfully saved to '{persist_directory}'.")
    return vector_store



def setup_rag_chain(persist_directory, azure_configs):
    """Sets up and returns a simple RAG chain using Azure OpenAI and Chroma."""

    # Load embeddings and vector store
    embedding_config = azure_configs["embedding"]
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=embedding_config["deployment"],
        azure_endpoint=embedding_config["endpoint"],
        api_key=embedding_config["api_key"],
        api_version=embedding_config["api_version"],
    )
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})


    # Initialize chat model
    chat_config = azure_configs["chat"]
    llm = AzureChatOpenAI(
        azure_deployment=chat_config["deployment"],
        azure_endpoint=chat_config["endpoint"],
        api_key=chat_config["api_key"],
        api_version=chat_config["api_version"],
        temperature=0.7,
    )

    # Prompt template
    prompt_template = """
    Answer the user's question using only the provided context.
    If the answer is not in the context, say: "I cannot answer this question based on the provided document."

    CONTEXT:
    {context}

    QUESTION:
    {question}

    ANSWER:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])


    # Create the RAG chain
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return rag_chain
