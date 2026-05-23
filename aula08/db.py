from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Conectando a um banco de dados SQLite em memória
engine = create_engine('sqlite:///:memory:', echo=True)

#Criação da base declarativa
Base = declarative_base()

#Definição da classe (modelo) Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, idade={self.idade})"
    

#Criação
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


#Inserção de dados
usuario1 = Usuario(nome='João', idade=22)
usuario2 = Usuario(nome="Marcos", idade=24)
session.add(usuario1)
session.add(usuario2)

#commit das alterações
session.commit()

#consulta dos dados
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario)