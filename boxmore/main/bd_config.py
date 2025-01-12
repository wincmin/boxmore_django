import mysql.connector

def conecta_no_banco_de_dados():
    # Conectar ao servidor MySQL
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')
    cursor = cnx.cursor()

    # Verificar se o banco de dados 'boxmore_banco' existe
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "boxmore_banco";')
    num_results = cursor.fetchone()[0]

    # Fechar a conexão inicial
    cnx.close()

    # Se o banco de dados não existe, criá-lo
    if num_results == 0:
        # Conectar-se novamente ao servidor MySQL para criar o banco de dados
        cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')
        cursor = cnx.cursor()

        # Criar o banco de dados
        cursor.execute('CREATE DATABASE boxmore_banco;')
        cnx.commit()

        # Conectar-se ao banco de dados recém-criado
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='boxmore_banco'  # Especificar o banco de dados
        )
        cursor = cnx.cursor()

        # Criar as tabelas
        cursor.execute('''
            CREATE TABLE usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                nome VARCHAR(255), 
                email VARCHAR(255), 
                senha VARCHAR(255), 
                perfil VARCHAR(255)
            );
        ''')

        cursor.execute('''
            CREATE TABLE produto (
                id SERIAL PRIMARY KEY,
                nome_produto VARCHAR(200) NOT NULL,
                preco DECIMAL(10, 2) NOT NULL,
                marca VARCHAR(100),
                imagem VARCHAR(100),
                CONSTRAINT produto_nome_produto_key UNIQUE (nome_produto)
            );
        ''')

        # Inserir dados iniciais na tabela 'usuarios'
        nome = "Camille"
        email = "camz@gmail.com"
        senha = "12345"
        perfil = "administrador"
        sql = "INSERT INTO usuarios (nome, email, senha, perfil) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, senha, perfil)
        cursor.execute(sql, valores)
        cnx.commit()

        # Inserir dados iniciais na tabela 'produto'
        nome_produto = "Fone Bluetooth Preto"
        preco = 139.99
        marca = "JBL"
        imagem = "static/images/fone-bluetooth.jpg"

        sql = "INSERT INTO produto (nome_produto, preco, marca, imagem) VALUES (%s, %s, %s, %s)"
        valores = (nome_produto, preco, marca, imagem)

        cursor.execute(sql, valores)
        cnx.commit()

        # Fechar a conexão
        cursor.close()
        cnx.close()

    try:
        # Conectar ao banco de dados 'boxmore_banco' existente
        bd = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='boxmore_banco'
        )
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        raise

    return bd
