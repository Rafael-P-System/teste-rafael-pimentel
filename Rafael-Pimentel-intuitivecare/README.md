# Projeto Operadoras de Saúde 

Este projeto tem como objetivo consolidar e enriquecer dados de operadoras de saúde a partir de arquivos CSV, armazenando-os em um banco SQLite e permitindo consultas analíticas. Além disso, disponibiliza uma API em Flask e um frontend em Vue/Vite para visualização dos dados.



## 📂 Estrutura de Pastas

backend/
├── app.py                                # API Flask  
├── api.py                                # Rotas adicionais  
├── operadoras.db                         # Banco SQLite  
├── data/  
│   ├── consolidado_despesas.csv  
│   ├── operadoras.csv  
│   ├── init_db.py  
│   ├── seed.py  
│   ├── seed_enriquecido.py  
│   └── queries.py  
frontend/  
├── src/  
│   ├── components/  
│   │   ├── EstadosIBGE.vue  
│   │   ├── OperadorasTable.vue  
│   │   └── GraficoDespesas.vue  
│   └── services/  
│       └── api.js  



## ⚙️ Pré-requisitos

- Python 3.10+  
- Node.js 18+  
- Virtualenv configurado  
- Dependências:  
  - Backend: Flask, SQLAlchemy  
  - Frontend: Vue 3, Vite, Axios, Chart.js  

---

## 🚀 Como rodar o projeto

### 1. Backend (Flask)

Ativar ambiente virtual:
```powershell
& .venv\Scripts\Activate.ps1
Entrar na pasta backend:

powershell
cd Rafael-Pimentel-intuitivecare\backend
Instalar dependências:

bash
pip install -r requirements.txt
Rodar servidor Flask:

bash
python app.py
➡️ O backend estará disponível em: http://127.0.0.1:5000

2. Frontend (Vue/Vite)
Em outro terminal, entrar na pasta frontend:

powershell
cd Rafael-Pimentel-intuitivecare\frontend
Instalar dependências:

bash
npm install
Rodar servidor de desenvolvimento:

bash
npm run dev
➡️ O frontend estará disponível em: http://localhost:5173

3. Testando integração
Abra http://localhost:5173 no navegador.
O frontend vai consumir os endpoints do backend:

http://127.0.0.1:5000/api/operadoras

http://127.0.0.1:5000/api/estatisticas

📡 Endpoints da API
Endpoint	Método	Descrição
/api/operadoras	GET	Lista todas as operadoras
/api/operadoras/{cnpj}	GET	Detalhes de uma operadora específica
/api/estatisticas	GET	Estatísticas agregadas por UF
📊 Exemplos de Queries (SQLite)
Operadoras enriquecidas

Código
('12345678000199', 'Operadora Saúde RJ', 'RJ', 175000.0, 'ANS123', 'Medicina de Grupo')
('98765432000188', 'Operadora Saúde SP', 'SP', 225000.0, 'ANS987', 'Cooperativa Médica')
Top 5 operadoras por despesa acumulada

Código
('Operadora Saúde SP', 425000.0)
('Operadora Saúde RJ', 325000.0)
Média de despesas por UF

Código
('RJ', 175000.0)
('SP', 225000.0)

🖥️ Frontend
Tabela de Operadoras: lista CNPJ, razão social e UF.

Gráfico de Despesas por UF: barras mostrando valores consolidados.

Estados IBGE: lista de estados consumida da API pública do IBGE.

⚖️ Decisões Técnicas e Justificativas
Durante o desenvolvimento, algumas escolhas precisaram ser feitas. Abaixo explico o porquê de cada decisão, os prós e contras considerados e como isso se conecta ao contexto do teste.

Linguagem e Framework
Optamos por Python com Flask.
A escolha foi motivada pela simplicidade: Flask é leve, direto e tem uma curva de aprendizado pequena. Isso nos permitiu focar mais na lógica de negócio e menos em configuração. Reconhecemos que o FastAPI poderia oferecer melhor performance em cenários de alta concorrência, mas para o escopo do teste, a clareza e rapidez do Flask foram mais valiosas.

Banco de Dados
Usamos SQLite.
A decisão foi prática: não exige servidor externo, é fácil de configurar e perfeito para protótipos. Sabemos que em produção o ideal seria PostgreSQL ou MySQL, como o teste sugere, mas para validar o fluxo completo (integração, API, frontend) o SQLite foi suficiente. Isso reduziu a complexidade sem comprometer a análise.

Integração com APIs Externas
Consumimos dados da ANS e do IBGE.
A ideia foi centralizar no backend a responsabilidade de buscar e normalizar informações externas. Isso garante consistência e evita que o frontend precise lidar com formatos diferentes. O desafio foi lidar com estruturas variáveis e possíveis falhas de rede — nesses casos, optamos por tratar com mensagens claras e flags de inconsistência.

Paginação
Implementamos offset-based pagination.
É simples de entender e implementar, além de funcionar bem para o volume moderado de dados esperado. Reconhecemos que para bases muito grandes, estratégias como cursor-based seriam mais eficientes, mas aqui a prioridade foi clareza.

Estatísticas
Optamos por calcular as estatísticas diretamente nas queries.
Isso garante que os resultados estejam sempre atualizados. Em cenários com milhões de registros, consideraríamos cache ou pré-cálculo, mas para o tamanho atual dos dados, a simplicidade venceu.

Tratamento de Inconsistências
CNPJs inválidos: mantidos com flag de “suspeito”, para não perder rastreabilidade.

Valores negativos ou zerados: preservados, mas sinalizados como possíveis erros de origem.

Razões sociais diferentes para o mesmo CNPJ: mantivemos o mais recente e registramos divergência.

Registros sem match no cadastro da ANS: preservados com flag “não encontrado”.

CNPJs duplicados no cadastro: escolhemos o mais recente para simplificar.

Frontend (Vue + Vite)
Busca no servidor: garante consistência e evita sobrecarga no cliente.

Gerenciamento de estado com Props/Events: suficiente para o tamanho atual do projeto; em cenários maiores, migraríamos para Pinia.

Tratamento de erros e loading: mensagens claras para falhas de rede, indicadores visuais durante carregamento e mensagens específicas para dados vazios.

🌱 Possíveis Melhorias Futuras
Migrar o banco para PostgreSQL para maior robustez.

Implementar cache em estatísticas para otimizar performance.

Adotar Pinia para gerenciamento de estado no frontend.

Criar testes automatizados para validar integrações e consistência dos dados.

📝 Conclusão
Este projeto demonstra como consolidar dados de operadoras de saúde, enriquecer com informações cadastrais e disponibilizar consultas analíticas via API Flask e frontend Vue/Vite.
O fluxo está pronto para ser expandido em dashboards mais completos ou integrado a sistemas maiores.

📄 Licença
Este projeto é distribuído sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.