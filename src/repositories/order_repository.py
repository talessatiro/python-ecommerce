from typing import Dict, List, Optional
from src.domain.order import Order


class OrderRepository:
    """Repositório de persistência para pedidos."""

    def __init__(self) -> None:
        self._db: Dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self._db[order.id] = order

    def find_by_id(self, order_id: str) -> Optional[Order]:
        return self._db.get(order_id)

    def list_all(self) -> List[Order]:
        return list(self._db.values())

