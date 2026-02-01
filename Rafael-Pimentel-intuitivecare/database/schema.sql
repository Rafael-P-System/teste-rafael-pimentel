CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    registroans VARCHAR(20),
    modalidade VARCHAR(100),
    uf CHAR(2)
);

CREATE TABLE despesas_consolidadas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    razaosocial VARCHAR(# Completar schema.sql
Add-Content -Path "projeto-ituitivecare/database/schema.sql" -Value @'
    razaosocial VARCHAR(255) NOT NULL,
    trimestre VARCHAR(10) NOT NULL,
    ano INT NOT NULL,
    valordespesa DECIMAL(18,2) NOT NULL,
    FOREIGN KEY (cnpj) REFERENCES operadoras(cnpj)
);

CREATE TABLE despesas_agregadas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    razaosocial VARCHAR(255) NOT NULL,
    uf CHAR(2) NOT NULL,
    ano INT NOT NULL,
    trimestre VARCHAR(10) NOT NULL,
    total_despesas DECIMAL(18,2),
    media_trimestre DECIMAL(18,2),
    desvio_padrao DECIMAL(18,2)
);
