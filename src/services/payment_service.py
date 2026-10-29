from decimal import Decimal


class PaymentService:
    """Serviço de aplicação para processamento de pagamentos."""

    def process_payment(self, order_id: str, amount: Decimal) -> bool:
        if amount <= Decimal("0.00"):
            return False
        # Simulação de gateway de pagamento aprovado
        return True

