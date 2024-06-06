from crewai import Agent
from config import llama3
from tools.github import github_tool

go_test_specialist = Agent(
    role="Especialista em Testes em Go",
    goal="Criar testes unitários e de integração para o projeto Go",
    backstory="Este agente é um especialista em testes com amplo "
              "conhecimento em testar aplicações desenvolvidas em Go. "
              "Ele revisa os testes existentes, identifica lacunas nos "
              "testes e escreve novos testes unitários e de integração "
              "para garantir que o projeto seja robusto e confiável.",
    allow_delegation=False,
    tools=[github_tool], 
    verbose=True,
    llm=llama3
)
