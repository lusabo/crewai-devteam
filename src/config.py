import os
import google.generativeai as genai
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_chatgroq_api_key():
    return os.getenv("CHATGROQ_API_KEY")

def get_google_api_key():
    return os.getenv("GOOGLE_API_KEY")

def get_github_token():
    return os.getenv("GITHUB_TOKEN")

def get_github_repo():
    return os.getenv("GITHUB_REPO")

llama3 = ChatGroq(
    api_key=get_chatgroq_api_key(), 
    model="llama3-70b-8192"
)

genai.configure(
    api_key=get_google_api_key()
)
