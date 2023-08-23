import unittest
import sqlite3
from crudsqlite import criarAluno, atualizarAluno, listagemAluno


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
        criarAluno(self.conexao, "SILVA ROBERTO", 45, 56.2)
        alunos = self.conexao.execute("SELECT * FROM tb_alunos").fetchall()
        self.assertEqual(alunos[0][1], "SILVA")

    def teste_verificar_se_os_aluno_cadastrado_estão_na_mesmas_quantidades_armazenadas(self):
        criarAluno(self.conexao, "SILVA ROBERTO", 45, 56.2)
        criarAluno(self.conexao, "JEFFERSON DAVID", 45, 56.2)
        alunos = self.conexao.execute("SELECT * FROM tb_alunos").fetchall()
        self.assertEqual(len(alunos), 2)

    def teste_verificar_se_os_aluno_foi_alterado(self):
        criarAluno(self.conexao, "SILVA ROBERTO", 45, 56.2)
        criarAluno(self.conexao, "JEFFERSON DAVID", 45, 56.2)
        atualizarAluno(self.conexao, 1, "NAYANA ROBERTA", 56, 80.5)
        alunos = self.conexao.execute("SELECT * FROM tb_alunos").fetchall()
        self.assertEqual(alunos[0][1], "NAYANA ROBERTA")

    def teste_listagem(self):
        criarAluno(self.conexao, "PEDRO DA SILVA", 45, 56.2)
        criarAluno(self.conexao, "JEFFERSON DAVID", 45, 56.2)
        alunos = listagemAluno(self.conexao)
        self.assertEqual(len(alunos), 2)
