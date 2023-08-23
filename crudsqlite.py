import sqlite3 
from pathlib import Path 
ROOT_DIR = Path(__file__).parent 
BD_NAME  = 'bd.sqlite'
BD_FILE  = ROOT_DIR/BD_NAME 
TABLE_NAME = 'tb_alunos'
conexao = sqlite3.connect(BD_FILE)
cursor  = conexao.cursor()
cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
               '('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT NOT NULL,'
               'idaed INTEGER NOT NULL,'
               'peso REAL NOT NULL'
               ')'
               )
conexao.commit()
def criarAluno(nome,peso,idade):
    novoAluno = ("INSERT INTO FROM tb_aluno (nome,idade,peso) VALUES (nome =?, idade=? peso=?);",(nome,peso,idade))
    conexao.commit()
    print("Aluno cadastrado com sucesso!")





cursor.close()
conexao.close()