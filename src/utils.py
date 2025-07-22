import os
from dotenv import load_dotenv

def load_azure_configs():
    """
    Loads Azure OpenAI configuration from the .env file and returns as a dictionary.
    """
    load_dotenv()

    configs = {
        "embedding": {
            "endpoint": os.getenv("EMBEDDING_AZURE_OPENAI_ENDPOINT"),
            "api_key": os.getenv("EMBEDDING_AZURE_OPENAI_API_KEY"),
            "deployment": os.getenv("EMBEDDING_AZURE_OPENAI_DEPLOYMENT"),
            "api_version": os.getenv("EMBEDDING_AZURE_OPENAI_API_VERSION"),
        },
        "chat": {
            "endpoint": os.getenv("CHAT_AZURE_OPENAI_ENDPOINT"),
            "api_key": os.getenv("CHAT_AZURE_OPENAI_API_KEY"),
            "deployment": os.getenv("CHAT_AZURE_OPENAI_DEPLOYMENT"),
            "api_version": os.getenv("CHAT_AZURE_OPENAI_API_VERSION"),
        }
    }

    print("Azure OpenAI configuration loaded successfully.")

    return configs

