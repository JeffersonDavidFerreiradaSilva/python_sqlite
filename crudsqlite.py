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



def criarAluno(conexao,nome,idade,peso):
    novoAluno = conexao.execute ("INSERT INTO tb_alunos (nome,idade,peso) VALUES (?,?,?);",(nome,idade,peso))
    conexao.commit()
    print("Aluno cadastrado com sucesso!")
    return novoAluno



def listagemAluno(conexao):
    Alunos = conexao.execute("SELECT * FROM tb_alunos").fetchall()
    return Alunos


def atualizarAluno(conexao,id,nome,idade,peso):
    Atualizar = conexao.execute("UPDATE tb_alunos SET nome=?,idade=?,peso=? WHERE id=?",(nome,idade,peso,id))
    conexao.commit()
    print("Aluno Aprovado com Sucesso!")
    return Atualizar

def deletarAluno(id):
    deletar = conexao.execute("DELETE FROM tb_alunos WHERE id=?",(id,))
    conexao.commit()
    print("Aluno Deletado com Sucesso!")
#criarAluno("Nayna Roberta da Silva Pereira", 35, 60.5)
#atualizarAluno(2, "DAVID",60, 58.5)
#deletarAluno(1)
#listagemAluno()
cursor.close()
conexao.close()