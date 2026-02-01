import sqlite3

conn = sqlite3.connect("../operadoras.db")  
cursor = conn.cursor()

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS despesas_consolidadas (
    cnpj TEXT,
    razao_social TEXT,
    trimestre TEXT,
    ano INTEGER,
    valor_despesa REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS operadoras_cadastrais (
    cnpj TEXT PRIMARY KEY,
    registro_ans TEXT,
    modalidade TEXT,
    uf TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS despesas_agregadas (
    razao_social TEXT,
    uf TEXT,
    total_despesa REAL,
    media_trimestre REAL,
    proporcao REAL
)
""")

conn.commit()
conn.close()

print("Tabelas criadas com sucesso!")
