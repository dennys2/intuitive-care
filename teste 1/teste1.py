import requests
import os
from bs4 import BeautifulSoup

#Recebe um url e retorna um objeto BeautifulSoup
def requestUrl(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


#Entra no link da ultima versao 
def searchNewestVersion():
    soup = requestUrl('https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss')
    link = soup.find('a', class_='alert-link', href = True)
    url = link['href']
    return url


#Encontra o componente organizacional buscando a fileira correta na tabela HTML
def downloadComponente():
    url = searchNewestVersion()
    soup = requestUrl(url)
    rows = soup.tbody.contents
    componenteOrganizacionalRow = rows[1].find('a')
    urlToDownload = componenteOrganizacionalRow['href']
    fileName = urlToDownload.split('/')[-1]
    file = downloadFile(urlToDownload, fileName)
    print('File downloaded:', file)


#Salva o arquivo na pasta do projeto, dividindo em chunks (pedaços)
def downloadFile(url, filename):
    try:
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


downloadComponente()





