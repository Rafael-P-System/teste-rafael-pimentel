from fastapi import FastAPI, APIRouter
import sqlite3

app = FastAPI(title="API Operadoras de Saúde")
router = APIRouter(prefix="/api")

DB_PATH = "../operadoras.db"

def query_db(sql, params=()):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

@router.get("/operadoras")
def get_operadoras():
    sql = """
    SELECT cnpj, razao_social, uf, despesa, registro_ans, modalidade
    FROM operadoras_enriquecidas
    """
    return query_db(sql)

@router.get("/top-operadoras")
def get_top_operadoras():
    sql = """
    SELECT razao_social, SUM(valor_despesa) as total
    FROM despesas_consolidadas
    GROUP BY razao_social
    ORDER BY total DESC
    LIMIT 5
    """
    return query_db(sql)

@router.get("/crescimento")
def get_crescimento():
    sql = """
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
    """
    return query_db(sql)

@router.get("/media-uf")
def get_media_uf():
    sql = """
    SELECT uf, ROUND(AVG(despesa), 2) as media_despesa
    FROM operadoras_enriquecidas
    GROUP BY uf
    """
    return query_db(sql)

@router.get("/media-modalidade")
def get_media_modalidade():
    sql = """
    SELECT modalidade, ROUND(AVG(despesa), 2) as media_despesa
    FROM operadoras_enriquecidas
    GROUP BY modalidade
    """
    return query_db(sql)

app.include_router(router)
