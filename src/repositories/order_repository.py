from typing import Dict, List, Optional
from src.domain.order import Order


class OrderRepository:
    """Repositório de persistência para pedidos."""

    def __init__(self) -> None:
        self._db: Dict[str, Order] = {}

    def save(self, order: Order) -> Order:
        self._db[order.id] = order
        return order

    def find_by_id(self, order_id: str) -> Optional[Order]:
        return self._db.get(order_id)

    def list_by_customer(self, customer_id: str) -> List[Order]:
        return [o for o in self._db.values() if o.customer_id == customer_id]
