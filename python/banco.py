from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
mysql+mysqlconnector://<root>:<root>@<localhost>[:<3306>]/<energia>
engine = create_engine('mysql+mysqlconnector://root:root@localhost/energia')
def insertAno(insert):
    with Session(engine) as sessao: 
        ano = sessao.execute(text("INSERT INTO ano id_ano VALUES(?)"[insert]))
def insertPais(insert):
    with Session(engine) as sessao: 
        pais = sessao.execute(text("INSERT INTO pais id_pais VALUES(?)"[insert]))
def insertDado(insert):
    with Session(engine) as sessao: 
        dado = sessao.execute(text("INSERT INTO rel_pais_ano id_pais, id_ano, rel_dado VALUES(?)"[insert[0], insert[2], insert[1]]))