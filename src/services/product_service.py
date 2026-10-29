from typing import List, Optional
from src.domain.product import Product
from src.repositories.product_repository import ProductRepository


class ProductService:
    """Serviço de aplicação para consulta e catálogo de produtos.
    
    Atua como mediador da camada de aplicação, eliminando o acoplamento direto
    entre Presentation (ProductsRouter) e Infrastructure (ProductRepository).
    """

    def __init__(self, product_repository: Optional[ProductRepository] = None) -> None:
        self.product_repository = product_repository or ProductRepository()

    def list_products(self) -> List[Product]:
        """Recupera a lista de produtos disponíveis."""
        return self.product_repository.list_all()

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Busca um produto específico pelo identificador."""
        return self.product_repository.find_by_id(product_id)

