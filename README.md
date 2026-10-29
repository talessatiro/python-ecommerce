# Python E-Commerce Sample Repository

Repositório de exemplo em Python e FastAPI desenvolvido para a suíte de validação e testes da plataforma **Inova Code**.

## Estrutura do Código (`src/`)

```
src/
├── api/                          # Apresentação (FastAPI Routers)
│   ├── orders_router.py          # Conforme: chama OrderService
│   └── products_router.py        # [Cenário 2]: Violação acessando ProductRepository direto
├── services/                     # Aplicação (Orquestração de Regras de Negócio)
│   ├── order_service.py          # Orquestra pagamento e persistência
│   └── payment_service.py        # Validação financeira
│   # [Cenário 3]: notification_service.py ausente propositalmente (nó órfão planejado)
├── domain/                       # Domínio Puro
│   ├── order.py                  # Entidade Order e OrderItem
│   └── product.py                # Entidade Product
├── repositories/                 # Infraestrutura / Persistência
│   ├── order_repository.py       # Acesso a banco de pedidos
│   └── product_repository.py     # Acesso a catálogo de produtos
└── workers/                      # [Cenário 3]: Módulo implementado sem previsão no YAML
    └── analytics_worker.py       # Processador assíncrono não planejado
```
