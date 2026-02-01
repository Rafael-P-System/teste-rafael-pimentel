import sqlite3
import csv

conn = sqlite3.connect("../operadoras.db")
cursor = conn.cursor()

with open("consolidado_despesas.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cnpj = row["CNPJ"]
        razao_social = row["Razao Social"]
        trimestre = row["Trimestre"]
        ano = row["Ano"]
        valor = row["Valor despesa"]

        cursor.execute("""
        INSERT INTO despesas_consolidadas (cnpj, razao_social, trimestre, ano, valor_despesa)
        VALUES (?, ?, ?, ?, ?)
        """, (cnpj, razao_social, trimestre, ano, valor))

conn.commit()
conn.close()

print("Dados de despesas consolidadas inseridos com sucesso!")
