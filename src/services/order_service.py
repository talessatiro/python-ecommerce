from decimal import Decimal
from typing import List, Optional
import uuid

from src.domain.order import Order, OrderItem, OrderStatus
from src.repositories.order_repository import OrderRepository
from src.services.notification_service import NotificationService
from src.services.payment_service import PaymentService


class OrderService:
    """Serviço de aplicação que coordena o fluxo de checkout e pedidos."""

    def __init__(
        self,
        order_repository: Optional[OrderRepository] = None,
        payment_service: Optional[PaymentService] = None,
        notification_service: Optional[NotificationService] = None,
    ) -> None:
        self.order_repository = order_repository or OrderRepository()
        self.payment_service = payment_service or PaymentService()
        self.notification_service = notification_service or NotificationService()

    def create_order(self, customer_id: str, items_data: List[dict]) -> Order:
        items = [
            OrderItem(
                product_id=it["product_id"],
                quantity=it["quantity"],
                unit_price=Decimal(str(it["unit_price"])),
            )
            for it in items_data
        ]
        order = Order(
            id=f"ord-{uuid.uuid4().hex[:8]}",
            customer_id=customer_id,
            items=items,
            status=OrderStatus.PENDING,
        )

        # Processar pagamento via PaymentService
        paid = self.payment_service.process_payment(order.id, order.total_amount)
        if paid:
            order.mark_as_paid()
            # Disparar notificação assíncrona ao cliente via NotificationService
            self.notification_service.send_order_confirmation(
                order_id=order.id,
                customer_id=order.customer_id,
                total_amount=order.total_amount,
            )

        # Persistir no OrderRepository
        self.order_repository.save(order)
        return order

    def get_order(self, order_id: str) -> Optional[Order]:
        return self.order_repository.find_by_id(order_id)

