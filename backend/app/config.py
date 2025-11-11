"""
应用配置
"""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """应用设置"""
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # CORS配置
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./resume_optimizer.db"
    
    # Ollama配置
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"  # 默认模型
    
    # OpenAI配置（可选）
    OPENAI_API_KEY: str = ""
    USE_OPENAI: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

