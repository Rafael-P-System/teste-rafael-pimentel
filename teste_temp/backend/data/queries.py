import sqlite3

conn = sqlite3.connect("../operadoras.db")
cursor = conn.cursor()

print("Operadoras enriquecidas:")
cursor.execute("""
SELECT cnpj, razao_social, uf, despesa, registro_ans, modalidade
FROM operadoras_enriquecidas
""")
for row in cursor.fetchall():
    print(row)

print("\nTop 5 operadoras por despesa acumulada:")
cursor.execute("""
SELECT razao_social, SUM(valor_despesa) as total
FROM despesas_consolidadas
GROUP BY razao_social
ORDER BY total DESC
LIMIT 5
""")
for row in cursor.fetchall():
    print(row)

print("\nCrescimento percentual por operadora (último trimestre vs primeiro):")
cursor.execute("""
WITH base AS (
    SELECT cnpj, razao_social, trimestre, ano, valor_despesa,
           ROW_NUMBER() OVER (PARTITION BY cnpj ORDER BY ano, trimestre) as ordem
    FROM despesas_consolidadas
)
SELECT b1.razao_social,
       ROUND(((b2.valor_despesa - b1.valor_despesa) / b1.valor_despesa) * 100, 2) as crescimento_percentual
FROM base b1
JOIN base b2 ON b1.cnpj = b2.cnpj AND b2.ordem = (SELECT MAX(ordem) FROM base WHERE cnpj = b1.cnpj)
WHERE b1.ordem = 1
""")
for row in cursor.fetchall():
    print(row)

print("\nMédia de despesas por UF:")
cursor.execute("""
SELECT oe.uf, ROUND(AVG(oe.despesa), 2) as media_despesa
FROM operadoras_enriquecidas oe
GROUP BY oe.uf
""")
for row in cursor.fetchall():
    print(row)

print("\nMédia de despesas por modalidade:")
cursor.execute("""
SELECT modalidade, ROUND(AVG(despesa), 2) as media_despesa
FROM operadoras_enriquecidas
GROUP BY modalidade
""")
for row in cursor.fetchall():
    print(row)

conn.close()
