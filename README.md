## Testes intuitive-care

## ---- Teste 1 - WebScraping -----   Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo. 
### Tarefas de código:

    1.1 - Acessar o site: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss;
    1.2 - Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_201902.pdf);
    1.3 - Baixar o componente organizacional;

## ---- Teste 2 Transformação de dados ----- Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as ### tarefas de código abaixo.
### Tarefas de código:

    Extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
    Salvar dados em tabelas estruturadas, em csvs;
    e Zipar todos os csvs num arquivo "Teste_{seu_nome}.zip".

## ---- Teste 3 - Banco de dados -----Neste teste o candidato deverá criar scripts sql (MySQL 8. ou Postgres >10.0) que execute as tarefas de código abaixo.* 

### Tarefas de Preparação:

    Baixar os arquivos dos últimos 2 anos no repositório público : http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/ (pode ser feito manualmente)
    Baixar csv do link: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss (pode ser feito manualmente)

### Tarefas de código:

    Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação num banco MySQL ou Postgres (Atenção ao encoding dos arquivos!)
    Montar uma query analítica que traga a resposta para as seguintes perguntas:
        Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
        Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?

## ---- Teste 4 - FrontEnd -----Neste teste o candidato deverá criar uma interface web (usando o framework Vue.js) que se comunicará com um servidor em uma das linguagens mencionadas no fim desse email para realizar as tarefas de código abaixo.Tarefas de Preparação:

    Baixar csv do link: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss

### Tarefas de código:

    Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de preparação) e retorne as linhas que mais se assemelham
    Criar uma interface usando o framework Vue.js que permita a um usuário fazer essa pesquisa pelo browser
