import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER")
    OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def get_llm_config(cls):
        if cls.LLM_PROVIDER == "ollama":
            return {
                "model": cls.DEFAULT_MODEL,
                "base_url": cls.OLLAMA_HOST_URL
            }
        elif cls.LLM_PROVIDER == "openai":
            return {
                "model": cls.DEFAULT_MODEL,
                "api_key": cls.OPENAI_API_KEY
            }
        else:
            raise ValueError(f"Unsupported LLM provider: {cls.LLM_PROVIDER}")
