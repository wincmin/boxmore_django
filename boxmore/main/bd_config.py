import mysql.connector

def conecta_no_banco_de_dados():
   
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')
    cursor = cnx.cursor()

    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "boxmore_banco";')
    num_results = cursor.fetchone()[0]


    cnx.close()

 
    if num_results == 0:
        
        cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')
        cursor = cnx.cursor()

 
        cursor.execute('CREATE DATABASE boxmore_banco;')
        cnx.commit()

   
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='boxmore_banco' 
        )
        cursor = cnx.cursor()

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
        imagem = "static/fone-bluetooth.jpg"

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
