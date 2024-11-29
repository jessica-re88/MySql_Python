import mysql.connector

try:
    ligação = mysql.connector.connect(
        host="localhost",
        user="Jéssica",
        password="Jéssica2011",
        database="python4"
    )

    print('Ligação estabelecida com sucesso!')

    cursor = ligação.cursor()

    # Criação da tabela
    comando_sql = """
    CREATE TABLE IF NOT EXISTS clientes_ginásio(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT,
        peso INT,
        altura INT
    )
    """
    cursor.execute(comando_sql)

    # Inserção de dados
    comando_sql = 'INSERT INTO clientes_ginásio (nome, idade, peso, altura) VALUES (%s, %s, %s, %s)'
    dados = [
        ('Maria', 24, 82, 156),
        ('Guilherme', 35, 100, 178),
        ('Cleusa Maria', 55, 70, 169),
        ('Rafael', 23, 90, 185),
        ('José', 70, 77, 175)
    ]
    cursor.executemany(comando_sql, dados)
    ligação.commit()
    print('\nDados adicionados com sucesso!')

        
        