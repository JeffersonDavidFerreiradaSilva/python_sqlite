import unittest
import pymysql
from 

class TesteCrudsqlite (unittest.TestCase):
    def setUp(self):
        self.conexao = pymysql.connect(":memory:")

        self.conexao.execute("CREATE TABLE IF NOT EXISTS tb_alunos"
                             '('
                            'id INT NOT NULL AUTO_INCREMENT,'
                            'nome VARCHAR (50) NOT NULL,'
                            'idade INT NOT NULL,'
                            'peso FLOAT NOT NULL,'
                            'PRIMARY KEY (id)'
                            ')'
                             )

    def tearDown(self):
        self.conexao.close()

    def teste_verificar_se_o_aluno_cadastrado_e_o_mesmo_infomado(self):
        criarAluno(self.conexao, "SILVA ROBERTO", 45, 56.2)
        alunos = self.conexao.execute("SELECT * FROM tb_alunos").fetchall()
        self.assertEqual(alunos[0][1], "SILVA")

   