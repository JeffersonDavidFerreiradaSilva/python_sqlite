import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '@Cursos21',
    database = 'serpro'
)

TABLE_NAME = 'tb_alunos'
TABLE_NAME_2 = 'tb_endereco'


cursor = conexao.cursor()

cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} "
               '('
               'id INT NOT NULL AUTO_INCREMENT,'
               'nome VARCHAR (50) NOT NULL,'
               'idade INT NOT NULL,'
               'peso FLOAT NOT NULL,'
               'PRIMARY KEY (id)'
               ')'
              )
cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME_2} "
               '('
               'id INT NOT NULL AUTO_INCREMENT,'
               'rua VARCHAR (50) NOT NULL,'
               'numero INT NOT NULL,'
               'PRIMARY KEY (id),'
               'FOREIGN KEY (id) REFERENCES tb_alunos(id)'
               ')'
              )