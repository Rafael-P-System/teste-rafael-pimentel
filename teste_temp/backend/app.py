from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///operadoras.db'
db = SQLAlchemy(app)

class Operadora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    razao_social = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    despesa = db.Column(db.Float, nullable=False)

@app.route("/api/operadoras")
def listar_operadoras():
    operadoras = Operadora.query.all()
    return jsonify([{
        "cnpj": o.cnpj,
        "razao_social": o.razao_social,
        "uf": o.uf
    } for o in operadoras])

@app.route("/api/operadoras/<cnpj>")
def detalhes_operadora(cnpj):
    o = Operadora.query.filter_by(cnpj=cnpj).first_or_404()
    return jsonify({
        "cnpj": o.cnpj,
        "razao_social": o.razao_social,
        "uf": o.uf,
        "despesa": o.despesa
    })

@app.route("/api/estatisticas")
def estatisticas():
    total = db.session.query(func.sum(Operadora.despesa)).scalar() or 0
    media = db.session.query(func.avg(Operadora.despesa)).scalar() or 0
    por_uf = db.session.query(Operadora.uf, func.sum(Operadora.despesa))\
        .group_by(Operadora.uf).all()

    return jsonify({
        "total": total,
        "media": media,
        "por_uf": {uf: valor for uf, valor in por_uf}
    })

if __name__ == "__main__":
    app.run(debug=True)
