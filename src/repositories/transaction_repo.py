from typing import List
from src.models.transaction import Transaction
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository

class TransactionRepository(SQLAlchemyRepository[Transaction]):
    """
    Repositório especializado para transações financeiras.
    Oferece métodos adicionais para consultas específicas de usuários.
    """

    def list_by_user(self, user_id: int) -> List[Transaction]:
        """
        Retorna todas as transações pertencentes a um usuário específico.

        Args:
            user_id (int): ID do usuário.

        Returns:
            list[Transaction]: Lista de transações do usuário.
        """
        return [t for t in self.list_all() if t.user_id == user_id]
