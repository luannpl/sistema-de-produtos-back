import mysql.connector
import os
from dotenv import load_dotenv
from src.database.tabelas import criar_tabelas

# Carregar as variáveis de ambiente
# load_dotenv()

# # Dados de conexão com o banco de dados
# host = os.getenv("DB_HOST")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# porta = int(os.getenv("DB_PORT", 32461))




def criar_conexao():
    # Criar uma conexão com o banco de dados
    conexao = mysql.connector.connect(
    host="junction.proxy.rlwy.net",
    user="root",
    password="UOhlaseowyczpaUnZpPhmMbfCsvfNSiC",
    port=32461,
    database="railway"
)
    cursor = conexao.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS railway")
        cursor.execute("USE railway")
        criar_tabelas(cursor)
    except Exception as erro:
        print(f"{erro}: Erro ao criar o banco de dados")
    return conexao