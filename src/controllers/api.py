from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.repositories.db import SessionLocal, init_db
from src.repositories.transaction_repo import TransactionRepository
from src.models.transaction import Transaction
from src.utils.logger import get_logger

app = FastAPI(title="FinTrack API")
log = get_logger("API")

def get_db() -> Session:
    """
    Dependência do FastAPI para fornecer uma sessão de banco por requisição.
    Fecha a sessão automaticamente ao final.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup() -> None:
    """Evento executado na inicialização da API."""
    init_db()
    log.info("API inicializada e banco configurado.")

@app.get("/health")
def health() -> dict[str, str]:
    """Verifica o estado da aplicação."""
    return {"status": "ok"}

@app.get("/transactions")
def list_transactions(db: Session = Depends(get_db)) -> list[dict]:
    """
    Lista todas as transações do banco de dados.

    Args:
        db (Session): Sessão SQLAlchemy injetada pelo FastAPI.

    Returns:
        list[dict]: Lista de transações em formato JSON serializável.
    """
    repo = TransactionRepository(Transaction, db)
    txs = repo.list_all()
    log.info(f"{len(txs)} transações retornadas.")
    return [t.__dict__ for t in txs]
