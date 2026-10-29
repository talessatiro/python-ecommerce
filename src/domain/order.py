from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class OrderItem:
    """Item individual de um pedido."""

    product_id: str
    quantity: int
    unit_price: Decimal

    @property
    def total(self) -> Decimal:
        return self.unit_price * Decimal(self.quantity)


@dataclass
class Order:
    """Entidade central do agregado de Pedido."""

    id: str
    customer_id: str
    items: List[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING

    @property
    def total_amount(self) -> Decimal:
        return sum((item.total for item in self.items), Decimal("0.00"))

    def mark_as_paid(self) -> None:
        if self.status != OrderStatus.PENDING:
            raise ValueError(f"Pedido no status {self.status} não pode ser pago.")
        self.status = OrderStatus.PAID
