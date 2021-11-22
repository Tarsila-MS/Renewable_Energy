from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine('mysql+mysqlconnector://root:root@localhost/renewableenergy')

def insertPaises(nomes):
    paises = {}
    sessao = Session(engine)
    try:
        parametros = {
            'nome_pais': ''
        }
        for nome in nomes:
            parametros['nome_pais'] = nome
            sessao.execute(text("INSERT INTO pais (nome_pais) VALUES(:nome_pais)"), [parametros])
            paises[nome] = sessao.execute("SELECT last_insert_id() id").first().id   
        sessao.commit()
    finally:
        sessao.close()
    return paises

def insertProducao(paises, dados):
    sessao = Session(engine)
    try:
        parametros = {
            'id_pais': paises[dados[0]],
            'ano': dados[2],
            'producao': dados[1]
        }
        sessao.execute(text("INSERT INTO pais_producao (id_pais, ano, producao) VALUES(:id_pais, :ano, :producao)"), [parametros])
        sessao.commit()
    finally:
        sessao.close()
