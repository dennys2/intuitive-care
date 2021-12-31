import requests
import os
from bs4 import BeautifulSoup

#Recebe um url e retorna um objeto BeautifulSoup
def requestUrl(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


#entra no link da ultima versao 
soup = requestUrl('https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss')
link = soup.find('a', class_='alert-link', href = True)
url = link['href']
print(url)

soup = requestUrl(url)
rows = soup.tbody.contents
componenteOrganizacionalRow = rows[1].find('a')
urlToDownload = componenteOrganizacionalRow['href']
fileName = urlToDownload.split('/')[-1]
print(urlToDownload)





