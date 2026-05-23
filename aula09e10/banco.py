from marca import Marca
from pessoa import Pessoa
from veiculo import Veiculo
from datetime import date
import os
import sqlite3
import logging


logging.basicConfig(
    filename="main.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)


class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa(
                    cpf INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    nascimento DATE,
                    oculos BOOLEAN
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela Pessoa: {e}")

    def criar_tabela_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca(
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    sigla TEXT
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela Marca: {e}")

    def criar_tabela_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo(
                    placa TEXT PRIMARY KEY,
                    cor TEXT NOT NULL,
                    cpf_proprietario INTEGER,
                    id_marca INTEGER,
                    FOREIGN KEY(cpf_proprietario) REFERENCES Pessoa(cpf)
                    FOREIGN KEY(id_marca) REFERENCES Marca(id)
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Veiculo {e}")

    def inserir_pessoa(self, pessoa:Pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Pessoa VALUES(?, ?, ?, ?)",(
                    pessoa.cpf,
                    pessoa.nome,
                    pessoa.nascimento,
                    pessoa.oculos,
                ),)
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir pessoa: {e}")


    def inserir_veiculo(self, veiculo:Veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Veiculo VALUES(?, ?, ?, ?)",(
                        veiculo.placa,
                        veiculo.cor,
                        veiculo.proprietario.cpf,
                        veiculo.marca.id,
                    ),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir veículo: {e}")

    def inserir_marca(self, marca:Marca):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Marca VALUES(?, ?, ?)",(
                        marca.id,
                        marca.nome,
                        marca.sigla,
                    ),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir marca: {e}")

    def atualizar_pessoa(self, pessoa:Pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE Pessoa SET nome=?, nascimento=?, oculos=?, WHERE cpf=?",
                    (pessoa.nome, pessoa.nascimento, pessoa.oculos, pessoa.cpf),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao atualizar pessoa: {e}")
    
    def atualizar_veiculo(self, veiculo:Veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE Veiculo SET cor=?,cpf_proprietario=?, id_marca=? WHERE placa=?",(
                        veiculo.cor,
                        veiculo.proprietario.cpf,
                        veiculo.marca.id,
                        veiculo.placa,
                    ),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao atualizar veiculo: {e}")

    def atualizar_marca(self, marca:Marca):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE Marca SET nome=?, sigla=? WHERE id=?",(
                        marca.nome,
                        marca.sigla,
                        marca.id
                    ),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao atualizar marca: {e}")

    def apagar_pessoa(self, pessoa:Pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "DELETE FROM Pessoa WHERE cpf=?",(pessoa.cpf,)
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao apagar a pessoa: {e}")

    def apagar_veiculo(self, veiculo:Veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "DELETE FROM Veiculo WHERE placa=?",(veiculo.placa,)
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao apagar veiculo: {e}")

    def apagar_marca(self, marca:Marca):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "DELETE FROM Marca WHERE id=?",(marca.id,)
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao apagar marca: {e}")


    def buscar_todas_pessoas(self):
        pessoas = []
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa")
                for row in cursor.fetchall():
                    cpf, nome, nascimento, oculos = row
                    pessoas.append(Pessoa(cpf, nome, nascimento, oculos))
            except sqlite3.Error as e:
                print(f"Erro ao buscar pessoas: {e}")
        return pessoas
    
    def buscar_todos_veiculos(self):
        veiculos = []
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Veiculo")
                for row in cursor.fetchall():
                    placa, cor, cpf_proprietario, id_marca = row
                    proprietario = self.buscar_pessoa_por_cpf(cpf_proprietario)
                    marca = self.buscar_marca_por_id(id_marca)
                    veiculos.append(Veiculo(placa, cor, proprietario, marca))
            except sqlite3.Error as e:
                print(f"Erro ao buscar veiculos: {e}")
        return veiculos
    
    def buscar_todas_marcas(self):
        marca =[]
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Marca")
                for row in cursor.fetchall():
                    id, nome, sigla = row
                    marca.append(Marca(id,nome,sigla))
            except sqlite3.Error as e:
                print(f"Erro a buscar marcas: {e}")
        return marca


    def buscar_pessoa_por_cpf(self, cpf:int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa WHERE cpf=?",(cpf,))
                row = cursor.fetchone()
                if row:
                    cpf, nome, nascimento, oculos = row
                    return Pessoa(cpf, nome, nascimento, oculos)
            except sqlite3.Error as e:
                print(f"Erro ao buscar a pessoa: {e}")


    def buscar_marca_por_id(self, id:int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Marca WHERE id=?",(id,))
                row = cursor.fetchone()
                if row:
                    id, nome, sigla = row
                    return Marca(id, nome, sigla)
            except sqlite3.Error as e:
                print(f"Erro ao buscar marca: {e}")

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None


    def criar_tabelas(self):
        self.criar_tabela_pessoa()
        self.criar_tabela_marca()
        self.criar_tabela_veiculo()
