import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get('https://www.amazon.com.br/')
sleep(1)
amazon = navegador.find_element('xpath', '//*[@id="twotabsearchtextbox"]')
amazon.click()
sleep(1)
amazon.send_keys('iphone')
sleep(1)
amazon.send_keys(Keys.ENTER)
sleep(2)

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
file_name = 'PesquisaAmazom.xlsx'
df.to_excel(file_name)
print('Informaçoes salvas.')
