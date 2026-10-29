from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Product:
    """Entidade de Produto do catálogo."""

    id: str
    sku: str
    name: str
    price: Decimal
    is_active: bool = True
    stock_quantity: int = 0
