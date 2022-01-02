import tabula
from zipfile import ZipFile

#Extrai os quadros 30, 31 e 32, dado o link e o intervalo das páginas
def extractPDF(path, pagesInterval):
    dfs = tabula.read_pdf(path, pages=pagesInterval) #Retorna um dataframe
    i=0
    for df in dfs:
        if ('Tabela' in df.iloc[0].to_string()): #Se o cabecalho possuir a palavra Tabela
            df.dropna(inplace=True) 
            df.to_csv('teste 2/' + quadros[i] + '.csv ', sep=';', encoding='utf-8', index=False, header=True) #Escreve/cria arquivo com nome do quadro.csv
            i=i+1 #Variável é incrementada para alterar posição do array de quadros
        else:
            df.to_csv('teste 2/' + quadros[1] + '.csv', mode='a', sep=';', encoding='utf-8', index=False, header=True) #Se não houver a palavra tabela no cabecalho
            #escreve em forma de append, dando continuidade e não apagando o csv em construcao
    zipCsv()


#Zipa todos os .csvs
def zipCsv():
    with ZipFile('teste 2/Teste_{Dennys_Lima}.zip', 'w') as zipObj: #Cria um arquivo .zip
        for quadro in quadros:
            zipObj.write('teste 2/' + quadro + '.csv')  #Escreve os csv dentro do arquivo .zip criado


quadros = ['Tabela de Tipo do Demandante', 'Tabela de Categoria do Padrão TISS', 'Tabela de Tipo de Solicitação'] #Array com os quadros 
pdf_path = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao-tiss_componente-organizacional_202111.pdf'
pages = '114-120' #Paginas selecionadas nos quais os quadros se localizam
extractPDF(pdf_path, pages)