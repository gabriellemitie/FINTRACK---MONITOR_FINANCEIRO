from src.models.category import Category
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository

class CategoryRepository(SQLAlchemyRepository[Category]):
    """
    Repositório específico para a entidade Category.
    Permite CRUD completo e extensões de lógica específicas para categorias.
    """
    pass
