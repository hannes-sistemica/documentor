import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    LLM_PROVIDER = os.getenv("LLM_PROVIDER")
    OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def get_llm_config(cls):
        if not cls.LLM_PROVIDER:
            raise ValueError("LLM_PROVIDER is not set in the environment variables")

        if cls.LLM_PROVIDER == "ollama":
            if not cls.OLLAMA_HOST_URL or not cls.DEFAULT_MODEL:
                raise ValueError("OLLAMA_HOST_URL or DEFAULT_MODEL is not set for Ollama provider")
            return {"model": cls.DEFAULT_MODEL, "base_url": cls.OLLAMA_HOST_URL}
        elif cls.LLM_PROVIDER == "openai":
            if not cls.OPENAI_API_KEY or not cls.DEFAULT_MODEL:
                raise ValueError("OPENAI_API_KEY or DEFAULT_MODEL is not set for OpenAI provider")
            return {"model": cls.DEFAULT_MODEL, "api_key": cls.OPENAI_API_KEY}
        else:
            raise ValueError(f"Unsupported LLM provider: {cls.LLM_PROVIDER}")

    @classmethod
    def get_db_connection_string(cls):
        return os.getenv('DATABASE_URL', f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}")
