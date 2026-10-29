from decimal import Decimal
from typing import Dict, List, Optional
from src.domain.product import Product


class ProductRepository:
    """Repositório de persistência para catálogo de produtos."""

    def __init__(self) -> None:
        self._db: Dict[str, Product] = {
            "prod-1": Product(id="prod-1", sku="SKU-001", name="Teclado Mecânico", price=Decimal("250.00"), stock_quantity=15),
            "prod-2": Product(id="prod-2", sku="SKU-002", name="Mouse Sem Fio", price=Decimal("120.00"), stock_quantity=30),
        }

    def find_by_id(self, product_id: str) -> Optional[Product]:
        return self._db.get(product_id)

    def list_all(self) -> List[Product]:
        return list(self._db.values())
