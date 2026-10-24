import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

def get_connection():
    database_path = os.getenv('DATABASE_PATH', 'database.db')

    db_connection = sqlite3.connect(database_path)
    # Acessa colunas por nome
    db_connection.row_factory = sqlite3.Row

    return db_connection

def init_db():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                hash_type TEXT NOT NULL
            )
        """)

        connection.commit()
    finally:
        connection.close()

if __name__ == '__main__':
    init_db()
    print('Tabela criada com sucesso!')
