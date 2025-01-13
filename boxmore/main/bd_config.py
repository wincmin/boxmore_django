import mysql.connector

def conecta_no_banco_de_dados():
    # Conectar ao servidor MySQL
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')

    # Criar o cursor para interagir com o banco de dados
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

        # Criar a tabela de usuarios com a coluna 'perfil'
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
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_produto VARCHAR(200) NOT NULL,
                preco DECIMAL(10, 2) NOT NULL,
                marca VARCHAR(100),
                imagem VARCHAR(100)
            );
        ''')

        # Criar a tabela carrinho
        cursor.execute('''
            CREATE TABLE carrinho (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT NOT NULL, 
                produto_id INT NOT NULL, 
                quantidade INT DEFAULT 1,
                status VARCHAR(100),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE, 
                FOREIGN KEY (produto_id) REFERENCES produto(id) ON DELETE CASCADE
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

        cnx.close()

    # Conectar ao banco de dados 'boxmore_banco' existente
    cnx = mysql.connector.connect(host='localhost', user='root', password='', database='boxmore_banco')
    cursor = cnx.cursor()

    # Verificar se a tabela 'produto' já contém dados
    cursor.execute("SELECT COUNT(*) FROM produto;")
    num_produtos = cursor.fetchone()[0]

    # Se não houver dados, insira os dados iniciais
    if num_produtos == 0:
        dados_produtos = [
            ('Fone Bluetooth JBL', 329.99, 'JBL', 'fone-bluetooth.jpg'),
            ('Jaqueta Masculina', 199.99, 'Men', 'jaqueta-masc.jpg'),
            ('Camiseta Marrom', 49.99, 'Z', 'camiseta-marrom.jpg'),
            ('Kindle', 249.99, 'Amazon', 'kindle.jpg')
        ]

        sql = "INSERT INTO produto (nome_produto, preco, marca, imagem) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, dados_produtos)
        cnx.commit()

    # Fechar a conexão
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