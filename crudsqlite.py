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
               'idade INTEGER NOT NULL,'
               'peso REAL NOT NULL'
               ')'
               )
conexao.commit()
def criarAluno(nome,idade,peso):
    novoAluno = conexao.execute ("INSERT INTO tb_alunos (nome,idade,peso) VALUES (?,?,?);",(nome,idade,peso))
    conexao.commit()
    print("Aluno cadastrado com sucesso!")

def listagemAluno():
    Alunos = conexao.execute("SELECT * FROM tb_alunos").fetchall()
    for aluno in Alunos:
        print(aluno)


listagemAluno()






#criarAluno("Nayna Roberta da Silva Pereira", 35, 60.5)



cursor.close()
conexao.close()