import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
import requests


url = 'https://www.amazon.com.br/s?k=iphone'
pesquisa = requests.get(url)
soup = BeautifulSoup(pesquisa.content, 'html.parser')
sleep(1)

itens = []
results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
sleep(1)
for result in results:
    nome_produto = result.h2.text
    try:
        preco1 = result.find('span', {'class': 'a-price-whole'}).text
        preco2 = result.find('span', {'class': 'a-price-fraction'}).text
        preco = (preco1 + preco2)
        itens.append([nome_produto, preco])
    except AttributeError:
        continue
sleep(2)
df = pd.DataFrame(itens, columns=['produto', 'preco'])
file_name = 'PesquisaAmazon.xlsx'
df.to_excel(file_name)
print('Informaçoes salvas.')
