from dotenv import load_dotenv
import os

load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:sample12@localhost/car_service_db")

# JWT Security Settings
SECRET_KEY = os.getenv("SECRET_KEY", "your_super_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
