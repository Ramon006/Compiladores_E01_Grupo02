# Entrega Semanal 02 — Linguagem de Diálogo para Chatbots (Grupo 02)

## Resumo
- Implementado módulo de **análise semântica** em `src/chatflow_semantic.py`.
- Criação explícita da **Tabela de Símbolos**, armazenando:
  - Estados declarados
  - Intenções conhecidas
  - Transições (`estado` → `intent` → `destino`)
- Validações principais:
  - Erro para **estados de destino inexistentes** em transições.
  - Erro para **intents desconhecidas** usadas em transições.
  - Aviso para **estados órfãos** (nunca alcançados a partir do estado inicial).
- Geração de relatórios legíveis de problemas, com indicação textual do ponto da falha.

## Arquivos relevantes
- `src/chatflow_semantic.py`
- `exemplos/valid.json`
- `exemplos/invalid.json`
- `tests/test_invalid_state.py`

## Próximos passos
- Integrar de forma mais clara o pipeline completo:
  - DSL (`.cf`) → IR (`.json`) → análise semântica → simulação.
- Começar a estudar uma forma de **visualizar o fluxo** em forma de diagrama textual.
