import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

# A quick safety check to ensure nothing is missing before the script runs
if not all([GEMINI_API_KEY, EMAIL_ADDRESS, EMAIL_APP_PASSWORD]):
    raise ValueError("Missing one or more environment variables. Please check your .env file.")