import unittest
import sqlite3
from crudsqlite import criarAluno
class TesteCrudsqlite (unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(":memory:")

        self.conexao.execute("CREATE TABLE IF NOT EXISTS tb_alunos"
                             '('
                             'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                             'nome TEXT NOT NULL,'
                             'idade INTEGER NOT NULL,'
                             'peso REAL NOT NULL'
                             ')'
                             )
    def tearDown(self):
        self.conexao.close()
    
    def teste_verificar_se_o_aluno_cadastrado_e_o_mesmo_infomado(self):
        criarAluno(self.conexao,"SILVA ROBERTO",45,56.2)
        alunos = self.conexao.execute("SELECT * FROM tb_alunos").fetchall()
        self.assertEqual(alunos[0][1],"SILVA")        

