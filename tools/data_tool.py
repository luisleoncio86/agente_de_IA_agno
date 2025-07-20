import pandas as pd

df = pd.read_csv("data/dados_de_vendas.csv", encoding="utf-8")

def query_dataframe(pergunta: str) -> str:
    """
    Responde perguntas sobre os dados do supermercado analisando o DataFrame.
    As colunas disponíveis são:
    - ID da Nota
    - Filial
    - Cidade
    - Tipo de Cliente
    - Gênero
    - Departamento
    - Preço Unitário
    - Quantidade
    - Imposto 5%
    - Total da Venda
    - Data
    - Hora
    - Forma de Pagamento
    - Custo das Mercadorias
    - Margem Bruta %
    - Lucro Bruto
    - Avaliação

    Exemplos de perguntas que a função está preparada para responder:
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
    - Qual cidade teve o maior faturamento para o gênero feminino?
    """
    pergunta = pergunta.lower()

    # Pergunta cruzada: cidade com maior total de vendas para mulheres
    if ("cidade" in pergunta and "maior" in pergunta and ("mulher" in pergunta or "feminino" in pergunta or "gênero feminino" in pergunta)):
        filtro = df[df["Gênero"].str.lower().str.contains("feminino")]
        grupo = filtro.groupby("Cidade")["Total da Venda"].sum()
        if grupo.empty:
            return "Não há vendas realizadas por mulheres na base de dados."
        cidade = grupo.idxmax()
        valor = grupo.max()
        return f"A cidade com maior total de vendas realizadas por mulheres é {cidade}, com R${valor:,.2f}."

    if "maior valor" in pergunta or "maior compra" in pergunta:
        row = df.loc[df['Total da Venda'].idxmax()]
        return f"A maior compra registrada foi de R${row['Total da Venda']:,.2f} na cidade de {row['Cidade']}."
    elif "faturamento total" in pergunta or "venda total" in pergunta:
        total = df["Total da Venda"].sum()
        return f"O faturamento total foi de R${total:,.2f}."
    elif "departamento mais vendido" in pergunta or "mais vendido" in pergunta:
        top = df["Departamento"].value_counts().idxmax()
        return f"O departamento mais vendido é: {top}."
    elif "média de vendas por cidade" in pergunta:
        medias = df.groupby("Cidade")["Total da Venda"].mean()
        return "Média de vendas por cidade:\n" + "\n".join([f"{cidade}: R${media:,.2f}" for cidade, media in medias.items()])
    elif "ticket médio" in pergunta:
        ticket = df["Total da Venda"].mean()
        return f"O ticket médio por venda é de R${ticket:,.2f}."
    elif "dinheiro" in pergunta and "venda" in pergunta:
        qtd = (df["Forma de Pagamento"] == "Dinheiro").sum()
        return f"Foram feitas {qtd} vendas em dinheiro."
    elif "avaliação média" in pergunta:
        media = df["Avaliação"].mean()
        return f"A avaliação média dos clientes é {media:.2f}."
    elif "total de vendas por gênero" in pergunta:
        vendas = df.groupby("Gênero")["Total da Venda"].sum()
        return "Total de vendas por gênero:\n" + "\n".join([f"{g}: R${v:,.2f}" for g, v in vendas.items()])
    elif "filial com maior faturamento" in pergunta:
        filial = df.groupby("Filial")["Total da Venda"].sum().idxmax()
        return f"A filial com maior faturamento é: {filial}."
    elif "produto menos vendido" in pergunta or "departamento menos vendido" in pergunta:
        dep = df["Departamento"].value_counts().idxmin()
        return f"O departamento menos vendido é: {dep}."
    elif "data com maior número de vendas" in pergunta:
        data = df["Data"].value_counts().idxmax()
        return f"A data com maior número de vendas foi: {data}."
    else:
        return "Desculpe, não consegui interpretar a pergunta. Tente reformular ou seja mais específico."
