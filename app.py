import streamlit as st
from src.utils import load_azure_configs
from src.rag_pipeline import setup_rag_chain

VECTOR_STORE_PATH = "vector_store"

st.set_page_config(page_title="RAG Chat", page_icon="🤖", layout="centered")


st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #8e44ad, #c0392b);
        color: white;
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    [data-testid="stTextInput"] label {
        color: white;
    }

    .stTextInput > div > div > input {
        background-color: #f0f2f6; 
        border-radius: 10px;
        border: 1px solid transparent;
        color: #31333F; 
    }
    
    .answer-box {
        background-color: rgba(0, 0, 0, 0.25); 
        border-radius: 10px;
        padding: 1rem 1.5rem;
        margin-top: 1rem;
    }

    .answer-label {
        color: #27ae60;
        font-weight: bold;
    }

    .answer-text {
        color: white;
        margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📄 Chat with Your Own Document")
st.write("Ask questions about your document and AI will answer your questions.")
st.write("---")

@st.cache_resource
def load_chain():
    try:
        azure_configs = load_azure_configs()
        rag_chain = setup_rag_chain(VECTOR_STORE_PATH, azure_configs)
        return rag_chain
    except Exception as e:
        st.error(f"An error occurred while loading the system: {e}")
        return None

rag_chain = load_chain()

if rag_chain:
    user_question = st.text_input("Your Question:")

    if user_question:
        with st.spinner("🔍 Searching and generating an answer..."):
            try:
                response = rag_chain.invoke(user_question)
                answer = response.content
                # Custom styled answer box
                st.markdown(f"""
                <div class="answer-box">
                    <p class="answer-label">✅ Answer:</p>
                    <p class="answer-text">{answer}</p>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred during querying: {e}")
