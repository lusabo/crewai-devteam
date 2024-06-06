import os
from dotenv import load_dotenv

load_dotenv()

def get_chatgroq_api_key():
    return os.getenv("CHATGROQ_API_KEY")

llama3 = ChatGroq(
    api_key=get_chatgroq_api_key(), 
    model="llama3-70b-8192"
)