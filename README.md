# 🤖 Agente Analista de Dados - Supermercado

Este projeto demonstra como criar um agente inteligente com o framework **Agno**, utilizando uma base de dados real de vendas de supermercado e integração com a OpenAI para análise flexível de dados.

## 🔧 Tecnologias usadas

- Python
- [Agno](https://github.com/agnostack/agno)
- OpenAI API
- Pandas
- Streamlit

## 📂 Estrutura do Projeto

```
.
├── data/
│   └── dados_de_vendas.csv
├── tools/
│   └── data_tool.py
├── main.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## ▶️ Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure sua chave da OpenAI no arquivo `.env`:
   ```
   OPENAI_API_KEY=sua-chave-aqui
   ```

3. Execute no terminal para usar via linha de comando:
   ```bash
   python main.py
   ```

4. Ou execute a interface web:
   ```bash
   streamlit run streamlit_app.py
   ```

## 💡 Exemplos de perguntas que o agente responde

- Qual cidade teve o maior valor de compra?
- Qual o faturamento total?
- Qual o departamento mais vendido?
- Qual a média de vendas por cidade?
- Qual foi o ticket médio por cliente?
- Quantas vendas foram feitas em dinheiro?
- Qual foi a avaliação média dos clientes?
- Qual o total de vendas por gênero?
- Qual a filial com maior faturamento?
- Qual o departamento menos vendido?
- Qual a data com maior número de vendas?
- Qual cidade tem o maior total de vendas realizadas por mulheres?
- De qual departamento os clientes do gênero feminino mais compram?

## 🌈 Interface Web

A interface web utiliza Streamlit e possui um visual escuro inspirado no ChatGPT, proporcionando uma experiência moderna e agradável para análise de dados.

---

Sinta-se à vontade para adaptar a base de dados e expandir as perguntas suportadas pelo agente!
