import pandas as pd
import plotly.express as px

# Constantes
VALOR_INICIAL = 2000
RATE = 100
STEPS = 50
LIMITE_MSC = 3500
PORCENTAGEM = 17 / 100

msc = {"Salário Bruto": [], "Recebido": [], "MSC": [], "Projeção": []}

# Cria a base de dados
for i in range(STEPS):
    valor = VALOR_INICIAL + (RATE * i)
    msc["Salário Bruto"].append(valor)
    if valor >= LIMITE_MSC:
        percent = valor * PORCENTAGEM
        msc["Recebido"].append(valor - percent)
        msc["MSC"].append(percent)
    else:
        msc["Recebido"].append(valor)
        msc["MSC"].append(0)
    msc["Projeção"].append(valor)

# Teste de conceito
# print(msc)

df = pd.DataFrame.from_dict(msc)

grafico = px.line(
    df, x="Salário Bruto", y=["Recebido", "MSC", "Projeção"], markers=True
)
grafico.show()
