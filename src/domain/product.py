from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    """Entidade do catálogo de produtos."""

    id: str
    sku: str
    name: str
    price: Decimal
    stock_quantity: int = 0

