import streamlit as st
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from tools.data_tool import query_dataframe

# Carrega variáveis de ambiente
dotenv_path = "C:/Users/Luis/Desktop/Projetos/Agente Agno BI/.env"
load_dotenv(dotenv_path=dotenv_path)

# Instancia o agente
agent = Agent(
    model=OpenAIChat(),
    tools=[query_dataframe]
)

# --- Customização do tema para fundo escuro e texto claro ---
custom_css = '''
<style>
html, body, [data-testid="stAppViewContainer"], .stApp {
    background-color: #343541 !important;
    color: #ececf1 !important;
}
section[data-testid="stSidebar"] {
    background-color: #202123 !important;
}
header, .st-emotion-cache-1avcm0n, .st-emotion-cache-1dp5vir, .st-emotion-cache-1v0mbdj {
    background: #343541 !important;
}
.st-emotion-cache-1v0mbdj, .st-emotion-cache-1dp5vir, .st-emotion-cache-1avcm0n {
    color: #ececf1 !important;
}
.stTextInput > div > div > input {
    background-color: #40414f !important;
    color: #ececf1 !important;
    border: 1px solid #565869 !important;
}
.stButton > button {
    background-color: #19c37d !important;
    color: #fff !important;
    border-radius: 6px;
    border: none;
    font-weight: bold;
}
.stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stDataFrame, .stTable, .stAlert, .stException, .stCodeBlock {
    color: #ececf1 !important;
}
</style>
'''
st.markdown(custom_css, unsafe_allow_html=True)

# --- Layout ---
st.title("🤖 Agente Analista de Dados")
st.write("Faça uma pergunta sobre os dados de vendas:")

pergunta = st.text_input("Pergunta:")

if st.button("Perguntar") and pergunta.strip():
    with st.spinner("Consultando..."):
        resposta = agent.run(pergunta)
        st.markdown("### Resposta do agente:")
        st.write(resposta.content)
