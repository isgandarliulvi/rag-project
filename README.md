\## 📄 Document Chatbot - Azure RAG Project

This project is a Retrieval-Augmented Generation (RAG) application that allows you to chat with your own PDF documents. Users can ask natural language questions about the uploaded document, and the AI—powered by Azure OpenAI services—generates answers based solely on the information contained in that document.



\## 🚀 Demo

!\[App Screen](images/screen.png)



\## 🛠️ Technology Stack



\* \*\*Backend \& AI:\*\* Python, LangChain

\* \*\*LLM \& Embeddings:\*\* Azure OpenAI

\* \*\*Database:\*\* ChromaDB (Local Vector Database)

\* \*\*Frontend:\*\* Streamlit

\* \*\*Dependency Management:\*\* Pip, venv



\## ⚙️ Installation and Setup



To run this project on your local machine, follow the steps below.



\### Prerequisites



\* Python 3.9+

\* An Azure account with configured OpenAI services (for both Embedding and Chat models).



\### 1. Clone the Repository



```bash

git clone https://github.com/\[your-username]/\[your-repo-name].git

cd \[your-repo-name]

```



\### 2. Create and Activate a Virtual Environment



```bash

\# Create the virtual environment

python -m venv venv



\# Activate the virtual environment (for Windows)

venv\\Scripts\\activate



\# Activate the virtual environment (for macOS/Linux)

\# source venv/bin/activate

```



\### 3. Install Required Libraries



```bash

pip install -r requirements.txt

```



\### 4. Set Up Environment Variables



The project requires your Azure API keys and endpoint information to communicate with the services.



\* In the project root directory, create a \*\*`.env`\*\* file.

\* Copy the following template into the `.env` file and replace the placeholders with your Azure details.



\# .env file template



\# --- EMBEDDING SERVICE DETAILS ---

EMBEDDING\_AZURE\_OPENAI\_ENDPOINT="\[embedding-service-endpoint]"

EMBEDDING\_AZURE\_OPENAI\_API\_KEY="\[embedding-service-api-key]"

EMBEDDING\_AZURE\_OPENAI\_DEPLOYMENT="\[embedding-model-deployment-name]"

EMBEDDING\_AZURE\_OPENAI\_API\_VERSION="2023-12-01-preview"



\# --- CHAT SERVICE DETAILS ---

CHAT\_AZURE\_OPENAI\_ENDPOINT="\[chat-service-endpoint]"

CHAT\_AZURE\_OPENAI\_API\_KEY="\[chat-service-api-key]"

CHAT\_AZURE\_OPENAI\_DEPLOYMENT="\[chat-model-deployment-name]"

CHAT\_AZURE\_OPENAI\_API\_VERSION="2023-12-01-preview"

```



\### 5. Add the Document



\* Place the PDF document you want to chat with inside the `data/` folder.

\* Update the `DATA\_PATH` variable in `ingest.py` with your file name (e.g., `data/sample\_document.pdf`).





\## 🚀 Usage



Running the project involves two main steps:



\### Step 1: Create the Vector Database



First, process your document and create a searchable vector database. This step only needs to be run once or whenever the document is updated.



```bash

python ingest.py

```



After completion, a `vector\_store` folder will be generated.



\### Step 2: Launch the Web Application



Once the database is ready, start the chat interface:



```bash

streamlit run app.py

```



This will automatically open a new tab in your browser, and you’ll be ready to chat with your document!











