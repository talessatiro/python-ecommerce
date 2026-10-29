from typing import Any, Dict, List

# [Cenário 2 - Violação Arquitetural Proposital]:
# A camada de apresentação (Presentation) NUNCA deve importar ou acoplar diretamente
# a camada de infraestrutura/persistência (Infrastructure). O correto seria passar por um ProductService.
from src.repositories.product_repository import ProductRepository


class ProductsRouter:
    """Controlador REST de produtos que introduz violação direta de camada (Presentation -> Infrastructure)."""

    def __init__(self, product_repository: ProductRepository | None = None) -> None:
        self.product_repository = product_repository or ProductRepository()

    def get_products(self) -> List[Dict[str, Any]]:
        # Acesso direto à persistência sem camada de serviço intermediária
        products = self.product_repository.list_all()
        return [
            {"id": p.id, "sku": p.sku, "name": p.name, "price": str(p.price)}
            for p in products
        ]

    def get_product_by_id(self, product_id: str) -> Dict[str, Any] | None:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return None
        return {"id": product.id, "sku": product.sku, "name": product.name, "price": str(product.price)}
