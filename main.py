import pandas as pd
import plotly.express as px

# Importa a tabela
tabela = pd.read_csv("telecom_users.csv")

# Ajusta os dados
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

#  Teste de conceito
teste = tabela.loc[:, ["Churn", "Casado"]].value_counts(normalize=True).loc[["Sim"], :]
teste_dict = teste.to_dict()

# Reserva valor de Churn total
# churn = tabela["Churn"].value_counts()["Sim"]

# Inicia dict para receber os dados
lookup_dict = {"Dado": [], "Churn": []}

# Para cada dado na tabela, retorna o maior influenciador no churn
for tag in tabela.columns:
    # Ignora colunas desnecessárias
    if tag != "Churn" and tag != "IDCliente":

        # Para cada dado, cria um pandas.Series que agrupa os dados com base no Churn
        aux_lookup = (
            tabela.loc[:, ["Churn", tag]].value_counts(normalize=True).loc[["Sim"], :]
        )

        # Converte os dados para dict e recupera os valores
        aux_dict = aux_lookup.to_dict()
        all_values = aux_dict.values()
        max_value = "{:.4}".format(max(all_values))
        max_key = max(aux_dict, key=aux_dict.get)

        lookup_dict["Dado"].append("{tag}: {key}".format(tag=tag, key=max_key[1]))
        lookup_dict["Churn"].append(float(max_value) * 100)

# Retorna a forma de pandas.DataFrame
analise = pd.DataFrame.from_dict(lookup_dict)

# Teste
print(analise)

# Plot do gráfico
grafico = px.histogram(
    analise,
    x="Dado",
    y="Churn",
    title="Relação Dados X Churn",
    labels=dict({"Dado": "Categoria", "Churn": "Churns"}),
    text_auto=True,
).update_xaxes(categoryorder="total ascending")
grafico.show()
