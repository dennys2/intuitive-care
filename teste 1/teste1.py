import requests
from bs4 import BeautifulSoup

#Recebe um url e retorna um objeto BeautifulSoup
def requestUrl(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


#Entra no link da ultima versao 
def searchNewestVersion():
    soup = requestUrl('https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss')
    link = soup.find('a', class_='alert-link', href = True) #Procura um elemento html alert-link
    url = link['href'] #Encontra o link que aponta para a próxima página
    return url


#Encontra o componente organizacional buscando a fileira correta na tabela HTML
def downloadComponente():
    url = searchNewestVersion()
    soup = requestUrl(url)
    rows = soup.tbody.contents #Retorna a tabela HTML
    componenteOrganizacionalRow = rows[1].find('a') #Retorna o elemento abaixo do cabeçalho, que é o que buscamos
    urlToDownload = componenteOrganizacionalRow['href'] #Encontra o link do pdf
    fileName = urlToDownload.split('/')[-1] #Pega o nome do pdf
    downloadFile(urlToDownload, fileName)
    print('File downloaded:', fileName)


#Salva o arquivo na pasta do projeto, dividindo em chunks (pedaços)
def downloadFile(url, filename):
    try:
        with requests.get(url) as req: 
            with open('teste 1/' + filename, 'wb') as f: #Escreve um arquivo dentro da pasta teste 1 com o nome do pdf baixado
                for chunk in req.iter_content(chunk_size=8192): #Itera o conteúdo em pedaços
                    if chunk:
                        f.write(chunk) #Escreve o pedaço
    except Exception as e:
        print(e)

downloadComponente()





