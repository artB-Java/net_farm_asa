from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship

# definindo a URL para conexão no banco
url = URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='102030',
    host='172.17.0.2',
    database='projeto_final_asa',
    port=5432
)

#url = "postgresql+psycopg2://postgres:banco@localhost/postgres"

# nesse ponto são instanciados os objetos para conexão com o banco
engine  = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True)
    dt_nascimento = Column(String, nullable=True)
    raca = Column(String)
    nome = Column(String, nullable=True)
    sexo = Column(String, nullable=True)
    idade = Column(Integer)
    categoria = Column(String)
    id_fazenda = Column(Integer, ForeignKey('fazenda.idFazenda'))

class Fazendeiro(Base):
    __tablename__ = 'fazendeiro'
    idFazendeiro = Column(Integer, primary_key=True)
    dt_nascimento = Column(String, nullable=True)
    nome = Column(String)
    sexo = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    contato = Column(String)
    email = Column(String)
    senha = Column(String)

class Fazenda(Base):
    __tablename__ = 'fazenda'
    idFazenda = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String, nullable=True)
    idFazendeiro = Column(Integer, ForeignKey('fazendeiro.idFazendeiro'))

class Ordenha(Base):
    __tablename__ = 'ordenha'
    idOrdenha = Column(Integer, primary_key=True)
    qtdLeite = Column(Float)
    dataOrdenha = Column(String, nullable=True)
    idAnimal = Column(Integer, ForeignKey('animal.id'))

class Pesagem(Base):
    __tablename__ = 'pesagem'
    idPesagem = Column(Integer, primary_key=True)
    peso = Column(Float)
    dataPesagem = Column(String, nullable=True)
    idAnimal = Column(Integer, ForeignKey('animal.id'))



Base.metadata.create_all(engine)


#docker run --name postgreSQL_SERVER -e POSTGRES_PASSWORD=banco -e POSTGRES_USER=postgres -p 5432:5432 -d postgres:14