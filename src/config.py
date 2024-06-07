import os
import google.generativeai as genai
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class EnvConfig:

    def __init__(self):
        load_dotenv()

        self.llama3 = ChatGroq(
            api_key=self.__get_chatgroq_api_key(), 
            model=self.__get_llm_model()
        )

        genai.configure(
            api_key=self.__get_google_api_key()
        )

    
    #Private
    def __get_llm_model(self):
        return os.getenv("LLM_MODEL")

    def __get_chatgroq_api_key(self):
        return os.getenv("CHATGROQ_API_KEY")

    def __get_google_api_key(self):
        return os.getenv("GOOGLE_API_KEY")

    #Public
    def get_llama3(self):
        return self.llama3
    
    def get_github_token(self):
        return os.getenv("GITHUB_TOKEN")

    def get_github_repo(self):
        return os.getenv("GITHUB_REPO")