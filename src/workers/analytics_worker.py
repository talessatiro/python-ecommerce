import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


# [Cenário 3 - Divergência Arquitetural / Componente Não Planejado]:
# Este módulo foi implementado pela equipe de engenharia para telemetria de eventos,
# porém NUNCA foi documentado ou incluído na especificação de arquitetura (01_architecture_spec.yaml).
# O Inova Code deve identificá-lo no snapshot implementado e reportar sua divergência.
class AnalyticsWorker:
    """Worker de telemetria assíncrona não previsto na especificação arquitetural."""

    def __init__(self) -> None:
        self.processed_events: int = 0

    def process_order_event(self, event_type: str, data: Dict[str, Any]) -> None:
        self.processed_events += 1
        logger.info("[ANALYTICS] Processando evento '%s': %s", event_type, data)
