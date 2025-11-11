import mysql.connector


def get_data(nome, email, senha):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = "root",
        password = '',
        database = 'login'
    )

    pointer = connection.cursor()
    pointer.execute('INSERT INTO users (nome, email, senha) values(%s, %s, %s)', (nome, email, senha))
    connection.commit()
    connection.close()


