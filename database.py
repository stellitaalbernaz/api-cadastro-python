import sqlite3
def conectar():
    return sqlite3.connect("usuarios.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (" \
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT, 
    email TEXT
    )
    """)
    conn.commit()
    conn.close