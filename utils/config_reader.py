from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_BASE_URL = os.getenv("API_BASE_URL")