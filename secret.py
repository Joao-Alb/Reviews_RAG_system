import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_customer_placeid():
    load_dotenv()
    return os.getenv("CUSTOMER_PLACE_ID")

def get_outscraper_api_key():
    load_dotenv()
    return os.getenv("OUTSCRAPER_API_KEY")