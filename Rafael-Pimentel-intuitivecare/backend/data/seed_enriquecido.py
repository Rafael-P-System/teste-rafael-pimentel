
import sqlite3
import csv

conn = sqlite3.connect("../operadoras.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS operadoras_enriquecidas (
    cnpj TEXT PRIMARY KEY,
    razao_social TEXT NOT NULL,
    telefone TEXT,
    uf TEXT,
    despesa REAL,
    registro_ans TEXT,
    modalidade TEXT
)
""")

# Carregar dados cadastrais (operadoras.csv)
cadastrais = {}
with open("operadoras.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        normalized = {k.strip().lower().replace(" ", ""): v for k, v in row.items()}
        cnpj = normalized.get("cnpj")
        cadastrais[cnpj] = {
            "registro_ans": normalized.get("registroans", ""),
            "modalidade": normalized.get("modalidade", ""),
            "uf": normalized.get("uf", ""),
            "razao_social": normalized.get("razaosocial", "")
        }

# Carregar consolidado (consolidado_despesas.csv)
with open("consolidado_despesas.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        normalized = {k.strip().lower().replace(" ", ""): v for k, v in row.items()}
        cnpj = normalized.get("cnpj")
        razao_social = normalized.get("razaosocial")
        telefone = normalized.get("telefone", "")
        uf = normalized.get("uf", "")
        despesa = normalized.get("valordespesa")  # agora pega corretamente

        dados_cadastrais = cadastrais.get(cnpj, {})
        registro_ans = dados_cadastrais.get("registro_ans", "")
        modalidade = dados_cadastrais.get("modalidade", "")
        uf_cadastral = dados_cadastrais.get("uf", uf)
        razao_social_cadastral = dados_cadastrais.get("razao_social", razao_social)

        cursor.execute("""
        INSERT OR REPLACE INTO operadoras_enriquecidas
        (cnpj, razao_social, telefone, uf, despesa, registro_ans, modalidade)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (cnpj, razao_social_cadastral, telefone, uf_cadastral, despesa, registro_ans, modalidade))

conn.commit()
conn.close()

print("Dados enriquecidos com sucesso!")
