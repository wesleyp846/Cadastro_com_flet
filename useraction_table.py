import sqlite3
import os

# Verificar se o diretório existe ou criá-lo se necessário
db_directory = 'db'
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Conectar ao banco de dados
conn = sqlite3.connect(os.path.join(db_directory, 'dbcad.db'), check_same_thread=False)

def create_table():
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            contact TEXT, 
            age INTEGER, 
            gender TEXT, 
            email TEXT, 
            address TEXT)""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro SQLite durante a criação da tabela: {e}")

# Chamar a função para criar a tabela
create_table()

# import sqlite3

# conn=sqlite3.connect('db/dbcads.db', check_same_thread=False)

# def create_table():
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS users 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         name TEXT, 
#         contact TEXT, 
#         age INTEGER, 
#         gender TEXT, 
#         email TEXT, 
#         address TEXT)""")    
#     conn.commit()
