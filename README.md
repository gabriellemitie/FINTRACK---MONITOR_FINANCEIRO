# 💰 FinTrack — Sistema Modular de Controle Financeiro Pessoal

Projeto acadêmico desenvolvido com Python + FastAPI + SQLAlchemy, seguindo arquitetura modular, injeção de dependências e Repository Pattern.

### Para monitoramento do progresso das atividades do grupo  
Inclui camadas separadas, tratamento de exceções, logs rotativos, mock de repositório para testes, e documentação técnica com type hints e docstrings completas. Parte Gabi  

## 🧩 Estrutura Geral do Projeto  

src/  
 ├── models/              # Entidades ORM (User, Category, Transaction)  
 ├── repositories/        # Camada de persistência e mock  
 ├── services/            # Lógica de negócio (injeção de dependência)  
 ├── controllers/         # API (FastAPI)  
 ├── utils/               # Logger e utilitários  
config/  
 ├── settings.py          # Leitura do .env e configuração global  
tests/                    # Testes unitários e de integração  
.logs/                    # Logs rotativos da aplicação  
fintrack.db               # Banco de dados SQLite local   

## 📦 Execução Completa
### 1️⃣ Ativar o ambiente:   
venv\Scripts\activate  

### 2️⃣ Iniciar banco:  
python -c "from src.repositories.db import init_db; init_db()"  

### 3️⃣ Rodar API:  
uvicorn src.controllers.api:app --reload  

### 4️⃣ Testar endpoints em:
/health  
/transactions  
/docs (Swagger UI)  


## 🧮 Banco de Dados e Modelos

O sistema utiliza três entidades relacionadas:

User: representa o usuário do sistema.  
Category: classifica as transações como Receita ou Despesa.  
Transaction: representa as movimentações financeiras e se relaciona com User e Category.  


## 🧱 Arquitetura e Padrões Aplicados

✅ Arquitetura modular com separação de camadas:  
Apresentação (controllers) → FastAPI  
Lógica de negócio (services) → classes e dependências  
Persistência (repositories) → Repository Pattern  

✅ Injeção de dependências:  
Sessões do banco são injetadas nas rotas via Depends(get_db)  
Serviços recebem os repositórios no construtor  

✅ Repository Pattern:
SQLAlchemyRepository: CRUD genérico  
UserRepository, CategoryRepository, TransactionRepository: específicos
MemoryRepository: mock para testes unitários  


## Instruções do projeto  
## 🧩 Configuração do Ambiente  
### 1️⃣ Criação do ambiente virtual:  
python -m venv venv  
venv\Scripts\activate  

### 2️⃣ Instalação das dependências:
pip install -r requirements.txt   

## 🧪 Testes Realizados
✅ Teste 1 — Inicialização do Banco  
python -c "from src.repositories.db import init_db; init_db()"  

Resultado esperado: ✅ Banco de dados inicializado com sucesso!

✅ Teste 2 — Criação de Usuário (CRUD real)  
python -c "from src.repositories.db import SessionLocal, init_db; from src.repositories.user_repo import UserRepository; from src.models.user import User; init_db(); s=SessionLocal(); repo=UserRepository(User,s); u=repo.add(User(name='Gabrielle',email='gabi@teste.com')); print('Usuário criado:',u.id,u.name); print('Todos:',repo.list_all())"  

Resultado esperado:   
Usuário criado: 1 Gabrielle
Todos: [<User(name=Gabrielle, email=gabi@teste.com)>]  

✅ Teste 3 — Tratamento de Exceção de Integridade  
python -c "from src.repositories.db import SessionLocal, init_db; from src.repositories.user_repo import UserRepository; from src.models.user import User; init_db(); s=SessionLocal(); repo=UserRepository(User,s); repo.add(User(name='Gabrielle',email='gabi@teste.com'))"  
Resultado esperado:  
ValueError: Erro de integridade ao inserir User: UNIQUE constraint failed: users.email

✅ Teste 4 — Mock do Banco (MemoryRepository)  
python -c "from src.repositories.memory_repo import MemoryRepository; from src.models.user import User; repo=MemoryRepository[User](); u=repo.add(User(name='Teste',email='mock@fake.com')); print('Usuário mock:',u.id,u.name); repo.update(u.id,name='Editado'); print('Depois do update:',repo.get(u.id).name); repo.delete(u.id); print('Após delete:',repo.list_all())"  
Resultado esperado:  
Usuário mock: 1 Teste  
Depois do update: Editado  
Após delete: []  

**📋 Mock funciona perfeitamente sem depender do banco físico.**  

✅ Teste 5 — API (FastAPI + Injeção de Dependência)  
uvicorn src.controllers.api:app --reload  
Verificar:  

http://127.0.0.1:8000/health  
 → {"status": "ok"}  

http://127.0.0.1:8000/transactions  
` → lista de transações  

http://127.0.0.1:8000/docs  
` → Swagger UI  

**📋 Confirma integração completa entre FastAPI, Repository e camada de persistência.**  

✅ Teste 6 — Logging  
python -c "from src.utils.logger import get_logger; log=get_logger('test'); log.debug('debug ativo'); log.info('sistema iniciado'); log.warning('aviso de teste'); log.error('erro simulado'); print('✅ Logs gerados em .logs/app.log')"  
 
Conteúdo esperado em .logs/app.log:  
2025-11-04 23:02:11 | INFO | fintrack.test | sistema iniciado  
2025-11-04 23:02:11 | WARNING | fintrack.test | aviso de teste   
2025-11-04 23:02:11 | ERROR | fintrack.test | erro simulado  





