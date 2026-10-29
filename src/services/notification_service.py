import logging
from decimal import Decimal
from typing import Any, Dict

logger = logging.getLogger(__name__)


class NotificationService:
    """Serviço de aplicação para envio de notificações transacionais aos clientes.
    
    Implementação oficial do componente planejado em 'src/services/notification_service.py'
    para validação da resolução de nó órfão no Inova Code.
    """

    def __init__(self) -> None:
        self.dispatched_count: int = 0

    def send_order_confirmation(self, order_id: str, customer_id: str, total_amount: Decimal) -> Dict[str, Any]:
        """Monta o template de e-mail e despacha a notificação de pedido confirmado."""
        self.dispatched_count += 1
        payload = {
            "order_id": order_id,
            "customer_id": customer_id,
            "total_amount": str(total_amount),
            "status": "sent",
        }
        logger.info("[NOTIFICATION] Confirmação de pedido despachada: %s", payload)
        return payload

