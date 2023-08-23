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
conexao.commit()
def criarAluno(nome,idade,peso):
    novoAluno = cursor.execute(F"INSERT INTO {TABLE_NAME} (nome,idade,peso) VALUES (%s,%s,%s)",(nome,idade,peso))
    conexao.commit()
    print("ALUNO CADASTRADO")


def listarAlunos():
    cursor.execute('SELECT * FROM tb_alunos')
    for Aluno in cursor.fetchall():
         print("Nome:", Aluno[1], "Idade:" , Aluno[2], "peso:" , Aluno[3])
    conexao.commit()

def atualizarAluno(id, nome,idade,peso):
    atualizar = cursor.execute("UPDATE tb_alunos SET nome=%s, idade=%s, peso=%s WHERE id=%s",(nome, idade, peso,id))
    conexao.commit()
    print("Aluno Atualizado com Sucesso! ")

def deletarAluno(id):
    deletar = cursor.execute("DELETE FROM tb_alunos WHERE id=%s",(id,))

criarAluno("NAYELLY ROBERT ADA SILVA PEREIRA", 49, 40.8)
atualizarAluno(4, "JOSE ROBERTA DA SILVA PEREIRA", 55, 75.5)
deletarAluno(9)
listarAlunos()