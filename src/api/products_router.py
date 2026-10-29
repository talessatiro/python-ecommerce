from typing import Any, Dict, List

# [Atualização v2 - Resolução da Violação de Camadas]:
# A camada de apresentação (Presentation) agora interage exclusivamente com a camada de
# aplicação (Application) através de 'ProductService', em estrita conformidade com a regra
# 'allowed_layer_dependencies: from presentation to application'.
from src.services.product_service import ProductService


class ProductsRouter:
    """Controlador REST de produtos refatorado para conformidade estrita de camadas."""

    def __init__(self, product_service: ProductService | None = None) -> None:
        self.product_service = product_service or ProductService()

    def get_products(self) -> List[Dict[str, Any]]:
        # Delegação conforme para o serviço da camada de aplicação
        products = self.product_service.list_products()
        return [
            {"id": p.id, "sku": p.sku, "name": p.name, "price": str(p.price)}
            for p in products
        ]

    def get_product_by_id(self, product_id: str) -> Dict[str, Any] | None:
        product = self.product_service.get_product_by_id(product_id)
        if not product:
            return None
        return {"id": product.id, "sku": product.sku, "name": product.name, "price": str(product.price)}

