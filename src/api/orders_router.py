from typing import Any, Dict, List
from src.services.order_service import OrderService


class OrdersRouter:
    """Controlador REST da camada de apresentação para pedidos (Conforme: chama OrderService)."""

    def __init__(self, order_service: OrderService | None = None) -> None:
        self.order_service = order_service or OrderService()

    def post_create_order(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        customer_id = payload.get("customer_id", "")
        items_data = payload.get("items", [])
        order = self.order_service.create_order(customer_id, items_data)
        return {
            "order_id": order.id,
            "status": order.status.value,
            "total_amount": str(order.total_amount),
        }

    def get_order_by_id(self, order_id: str) -> Dict[str, Any] | None:
        order = self.order_service.get_order(order_id)
        if not order:
            return None
        return {
            "order_id": order.id,
            "customer_id": order.customer_id,
            "status": order.status.value,
            "total_amount": str(order.total_amount),
        }

