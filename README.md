# Python E-Commerce Sample Repository (v2 - Refatorado e Conforme)

Repositório atualizado em Python e FastAPI desenvolvido para a suíte de validação e testes da plataforma **Inova Code**.

Esta versão (`repo-v2`) representa a **evolução arquitetural do repositório anterior (`repo/`)**, criada especificamente para validar a capacidade do Inova Code de detectar correções arquiteturais, resolução de nós órfãos e convergência de conformidade em re-execuções.

---

## 🎯 Principais Diferenças em Relação à Versão Anterior (`repo/`)

| Cenário Arquitetural | Estado no Repositório Anterior (`repo/`) | Estado nesta Versão Atualizada (`repo-v2/`) | Impacto Esperado no Cockpit do Inova Code |
|---|---|---|---|
| **Violação de Camadas** | `ProductsRouter` importava e acessava `ProductRepository` diretamente (`presentation -> infrastructure`). | `ProductsRouter` agora delega para `ProductService` (`src/services/product_service.py`), respeitando a fronteira de camadas. | Eliminação da aresta vermelha tracejada (`edge-invalid`). Redução de 1 para 0 violações críticas. Conformidade sobe para **100%**. |
| **Componente Órfão** | `NotificationService` estava ausente fisicamente do código (`src/services/notification_service.py`). | `NotificationService` implementado e acionado por `OrderService`. | Resolução do nó órfão (`node-planned` amarelo). Cobertura arquitetural sobe de 88.9% para **100%** (9 de 9 componentes). |
| **Divergência não Rastreada** | Módulo `AnalyticsWorker` estava presente sem especificação. | Removido / encapsulado em conformidade com o escopo do baseline arquitetural. | Redução do drift não planejado (+1 para 0). Saldo evolutivo limpo. |

---

## 📂 Estrutura do Código (`src/`)

```
src/
├── api/                          # Apresentação (FastAPI Routers)
│   ├── orders_router.py          # Conforme: chama OrderService
│   └── products_router.py        # [REFATORADO]: Agora consome ProductService (100% Conforme)
├── services/                     # Aplicação (Orquestração de Regras de Negócio)
│   ├── order_service.py          # Orquestra pagamento, notificação e persistência
│   ├── payment_service.py        # Validação financeira
│   ├── notification_service.py   # [NOVO]: Implementação de NotificationService (resolve nó órfão)
│   └── product_service.py        # [NOVO]: Serviço mediador para isolar acesso ao repositório
├── domain/                       # Domínio Puro
│   ├── order.py                  # Entidades Order, OrderItem e OrderStatus
│   └── product.py                # Entidade Product
└── repositories/                 # Infraestrutura / Persistência
    ├── order_repository.py       # Acesso e persistência de pedidos
    └── product_repository.py     # Acesso ao catálogo de produtos
```

---

## 🚀 Como Executar o Teste Comparativo no Inova Code

1. No Inova Code, crie ou edite o projeto apontando a URL/caminho do repositório para `docs/samples/python-ecommerce/repo-v2`.
2. Dispare uma nova execução do pipeline de 6 etapas.
3. Compare os resultados com o benchmark registrado em [`../EXPECTED_RESULTS.md`](../EXPECTED_RESULTS.md).

