from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

# Abre execução
navegador = webdriver.Chrome(executable_path=f'./chromedriver.exe')

# Busca cotações
navegador.get('https://www.google.com')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(f'cotação dólar')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

navegador.get('https://www.google.com')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(f'cotação euro')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

navegador.get('https://melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

print(cotacao_ouro)

navegador.quit()

# Leitura da base de dados

tabela = pd.read_excel(f'./Produtos.xlsx')

print(tabela)

# Edição da tabela

tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

tabela['Preço de Venda'] = tabela['Preço de Venda'].map('R$ {:.2f}'.format)
tabela['Preço de Compra'] = tabela['Preço de Compra'].map('R$ {:.2f}'.format)

print('')
print(tabela)

tabela.to_markdown('Produtos Novo.md')
