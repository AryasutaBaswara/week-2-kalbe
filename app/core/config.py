import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_TITLE: str = "Inventory API"
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

settings = Settings()