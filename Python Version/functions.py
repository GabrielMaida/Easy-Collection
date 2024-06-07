import mysql.connector
from sys import exit


def mainExecution():
    try:
        connect, cursor = openConnection()
        createDB(cursor)
        createTables(cursor)
        createCollection(connect, cursor)
        closeConnection(connect, cursor)
    except KeyboardInterrupt:
        print("\nExiting program...")
        exit()


def openConnection():
    try:
        host = input("Input the host: ")
        user = input("Input the user: ")
        password = input("Input the password: ")

        connection = mysql.connector.connect(host=host, user=user, password=password)

        cursor1 = connection.cursor()
        print("Connection stablished succesfully!")

        return connection, cursor1

    except Exception as error:
        if "2005 (HY000)" in str(error):
            print("Error: Unknown MySQL host")
            exit()
        elif "1045 (28000)" in str(error):
            print("Error: Incorrect user or password")
            exit()
        else:
            print("Error:", error)
            exit()


def closeConnection(connection, cursor1):
    try:
        if cursor1:
            cursor1.close()
            print("Cursor closed")

        if connection.is_connected():
            connection.close()
            print("Connection closed")

    except Exception as e:
        print("Error on closing connection:", e)


def createDB(cursor):
    db_name = input("Digite o nome do banco de dados a ser criado: ")
    try:
        print("Criando Banco de Dados...")

        # Execute a query para criar o banco de dados
        cursor.execute(f"CREATE DATABASE {db_name}")

        print(f"Banco de dados '{db_name}' criado com sucesso.")

        return None

    except mysql.connector.Error as e:
        # Verifique se o erro é devido a um banco de dados existente
        if "1007 (HY000)" in str(e):
            print(f"Banco de dados '{db_name}' já existe.")
        else:
            print(f"Erro: {e}")


def createTables(cursor):
    try:
        useDatabase = "use easycollection;"
        cursor.execute(useDatabase)

        createTableCollection = """CREATE TABLE `collection` (
      `id_collection` int NOT NULL AUTO_INCREMENT,
      `name_collection` varchar(70) NOT NULL,
      `dt_creation` date NOT NULL,
      PRIMARY KEY (`id_collection`),
      UNIQUE KEY `id_collection_UNIQUE` (`id_collection`),
      UNIQUE KEY `name_collection_UNIQUE` (`name_collection`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1"""
        cursor.execute(createTableCollection)

        createTableItem = """CREATE TABLE `item` (
      `id_item` int NOT NULL AUTO_INCREMENT,
      `name_item` varchar(70) NOT NULL,
      `dt_register` datetime NOT NULL,
      PRIMARY KEY (`id_item`),
      UNIQUE KEY `id_item_UNIQUE` (`id_item`),
      UNIQUE KEY `nome_item_UNIQUE` (`name_item`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1"""
        cursor.execute(createTableItem)

        createTableType = """CREATE TABLE `type_collection` (
      `id_type` int NOT NULL AUTO_INCREMENT,
      `name_type` varchar(45) NOT NULL,
      `description_type` varchar(150) DEFAULT NULL,
      PRIMARY KEY (`id_type`),
      UNIQUE KEY `id_type_UNIQUE` (`id_type`),
      UNIQUE KEY `name_type_UNIQUE` (`name_type`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1"""
        cursor.execute(createTableType)

        return None

    except mysql.connector.errors.Error as Error:
        print("Error:", str(Error))


def createCollection(connection, cursor):
    useDatabase = "use easycollection;"
    cursor.execute(useDatabase)

    nomeColecao = input("Digite o nome da coleção: ")

    queryCreateCollection = f"INSERT INTO collection (name_collection, dt_creation) VALUES (%s, CURDATE())"
    values = [nomeColecao]

    cursor.execute(queryCreateCollection, values)
    connection.commit()

    return None
