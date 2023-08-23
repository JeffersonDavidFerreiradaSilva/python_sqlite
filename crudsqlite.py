import sqlite3 
from pathlib import Path 
ROOT_DIR = Path(__DIR__).parent 
BD_NAME  = 'bd.sqlite'
BD_FILE  = ROOT_DIR/BD_NAME 
TABLE_NAME = 'tb_alunos'
conexao = sqlite3.connect(BD_FILE)
cursor  = conexao.cursor()
cursor.close()
conexao.close()