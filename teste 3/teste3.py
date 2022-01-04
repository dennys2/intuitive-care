import psycopg2

trimestres = ['1t2020', '1t2021', '2t2020', '2t2021', '3t2020', '3t2021', '4t2020']

def copiarTabelasTrimestrais(trimestres):
    try:
        for trimestre in trimestres:
            cur.execute(f"""
                CREATE TABLE trimestre{trimestre}(
                DATA DATE,
                REG_ANS text,
                CD_CONTA_CONTABIL text,
                DESCRICAO text,
                VL_SALDO_FINAL text
            )
            """)

            with open(f'teste 3/{trimestre}.csv', 'r') as f:
                next(f)
                cur.copy_from(f, f'trimestre{trimestre}', sep=';')
        copiarTabelaRegistro()
    except Exception as e:
        print(e)


def copiarTabelaRegistro():
    try:
        cur.execute("""
            CREATE TABLE registro(
            Registro_ANS text,
            CNPJ text,
            Razão_Social text,
            Nome_Fantasia text,
            Modalidade text,
            Logradouro text,
            Número text,
            Complemento text,
            Bairro text,
            Cidade text, 
            UF text,
            CEP text,
            DDD text,
            Telefone text,
            Fax text, 
            Endereço_eletrônico text,
            Representante text,
            Cargo_Representante text,
            Data_Registro_ANS DATE
        )
        """)
        with open(f'teste 3/Relatorio_cadop.csv', 'r') as f:
            next(f)
            cur.copy_from(f, f'registro', sep=';')
    except Exception as e:
        print(e)



try:
    conn = psycopg2.connect("dbname=teste3 user=postgres password=admin123")
    cur = conn.cursor()
except Exception as e:
    print(e)

copiarTabelaRegistro()

conn.commit()