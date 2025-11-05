from src.models.user import User
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository[User]):
    """
    Repositório específico para a entidade User.

    Herdado de SQLAlchemyRepository, fornece operações CRUD completas
    para o modelo User.
    """
    pass
