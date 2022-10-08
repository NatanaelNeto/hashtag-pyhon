from locale import normalize
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.csv")

tabela = tabela.drop("Unnamed: 0", axis=1)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

# Verifica, considerando os aposentados, qual o maior índice de churn
lookup1 = (
    tabela.loc[:, ["Churn", "Casado"]].value_counts(normalize=True).loc[["Sim"], :]
)

lookup1_dict = lookup1.to_dict()

# lookup1_normalize = lookup1.loc[["Sim"] == lookup1.max().item(), :]

# lookup1_percent = "{:.1%}".format(lookup1.max())

# print(lookup1_dict)


# Total de Churn na base de dados
churn = tabela["Churn"].value_counts()["Sim"]

# Verifica quais as maiores porcentagens de inferência em cada coluna, comparado com o Churn

lookup_dict = {"Dado": [], "Churn": []}

for tag in tabela.columns:
    if tag != "Churn" and tag != "IDCliente":
        aux_lookup = (
            tabela.loc[:, ["Churn", tag]].value_counts(normalize=True).loc[["Sim"], :]
        )
        aux_dict = aux_lookup.to_dict()
        all_values = aux_dict.values()
        max_value = "{:.4}".format(max(all_values))
        max_key = max(aux_dict, key=aux_dict.get)
        # print(tag, " -> ", max_key[1], " -> ", max_value)

        lookup_dict["Dado"].append("{tag}: {key}".format(tag=tag, key=max_key[1]))
        lookup_dict["Churn"].append(float(max_value) * 100)

# print(lookup_dict)

analise = pd.DataFrame.from_dict(lookup_dict)

print(analise)

grafico = px.histogram(
    analise,
    x="Dado",
    y="Churn",
    title="Relação Dados X Churn",
    labels=dict({"Dado": "Categoria", "Churn": "Churns"}),
    text_auto=True,
).update_xaxes(categoryorder="total ascending")
grafico.show()
