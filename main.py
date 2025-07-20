from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from tools.data_tool import query_dataframe

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path="C:/Users/Luis/Desktop/Projetos/Agente Agno BI/.env")

def main():
    print("🔍 Agente Analista de Dados do Supermercado (digite 'sair' para encerrar)")
    agent = Agent(
        model=OpenAIChat(),
        tools=[query_dataframe]
    )

    while True:
        question = input("\nPergunte algo sobre os dados: ")
        if question.lower() in ["sair", "exit"]:
            print("Até logo! 👋")
            break

        response = agent.run(question)
        print("\n📊 Resposta do agente:")
        print(response.content)

if __name__ == "__main__":
    main()
