import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class Config:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER")
    OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def get_llm_config(cls):
        logger.info(f"LLM_PROVIDER: {cls.LLM_PROVIDER}")
        logger.info(f"OLLAMA_HOST_URL: {cls.OLLAMA_HOST_URL}")
        logger.info(f"DEFAULT_MODEL: {cls.DEFAULT_MODEL}")
        logger.info(f"OPENAI_API_KEY set: {'Yes' if cls.OPENAI_API_KEY else 'No'}")

        if not cls.LLM_PROVIDER:
            raise ValueError("LLM_PROVIDER is not set in the environment variables")

        if cls.LLM_PROVIDER == "ollama":
            if not cls.OLLAMA_HOST_URL or not cls.DEFAULT_MODEL:
                raise ValueError("OLLAMA_HOST_URL or DEFAULT_MODEL is not set for Ollama provider")
            return {
                "model": cls.DEFAULT_MODEL,
                "base_url": cls.OLLAMA_HOST_URL
            }
        elif cls.LLM_PROVIDER == "openai":
            if not cls.OPENAI_API_KEY or not cls.DEFAULT_MODEL:
                raise ValueError("OPENAI_API_KEY or DEFAULT_MODEL is not set for OpenAI provider")
            return {
                "model": cls.DEFAULT_MODEL,
                "api_key": cls.OPENAI_API_KEY
            }
        else:
            raise ValueError(f"Unsupported LLM provider: {cls.LLM_PROVIDER}")
