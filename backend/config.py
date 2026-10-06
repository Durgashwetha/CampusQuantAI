import os
from pydantic import BaseModel

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class Settings(BaseModel):
    PROJECT_NAME: str = "CampusQuant AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # Secret Key for JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "campusquant_secret_key_2026_super_secure_jwt_token_auth")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 # 24 hours
    
    # Database Settings (XAMPP MySQL on localhost:3306, with SQLite fallback)
    MYSQL_DB_URL: str = os.getenv("MYSQL_DB_URL", "mysql+pymysql://root:@localhost:3306/campusquant_db")
    SQLITE_DB_URL: str = os.getenv("SQLITE_DB_URL", "sqlite:///./campusquant.db")
    
    # Groq API Keys Pool (Loaded from environment variables)
    GROQ_API_KEYS: list = [
        k.strip() for k in os.getenv("GROQ_API_KEYS", os.getenv("GROQ_API_KEY", "")).split(",") if k.strip()
    ]
    
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    GROQ_FALLBACK_MODEL: str = os.getenv("GROQ_FALLBACK_MODEL", "mixtral-8x7b-32768")

    # SMTP Gmail Email Credentials
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_EMAIL: str = os.getenv("SMTP_EMAIL", "campusquantai@gmail.com")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")

settings = Settings()
