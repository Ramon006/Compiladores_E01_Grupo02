# Entrega Semanal 03 — Linguagem de Diálogo para Chatbots (Grupo 02)

## Resumo
- Refinado o fluxo completo do compilador/interpretador ChatFlow:
  - DSL em `exemplos/chatflow_rules_example.cf`
  - Tradução para **IR JSON** com `tools/chatflow_to_json.py`
  - **Validação semântica** com `src/chatflow_semantic.py`
  - **Simulação interativa** de diálogos a partir da IR.
- Adicionado um módulo dedicado de **simulação visual em texto (fluxograma ASCII)**,
  permitindo visualizar todos os estados e transições de forma estática.

## Novidade: Visualização ASCII do fluxo
Foi criado o script:

- `tools/visualize_chatflow.py`

Função principal:
- Ler um arquivo de IR (por exemplo, `exemplos/from_rules.json` ou `exemplos/valid.json`).
- Imprimir no terminal um **fluxograma ASCII simples**, listando:
  - Cada estado
  - A resposta do estado (quando existir)
  - As transições de saída no formato:
    - `|--[intent]--> ProximoEstado`
  - Marcação de estados finais (sem transições).

Exemplo de uso:

```bash
python tools/visualize_chatflow.py exemplos/valid.json
```

## Próximos passos
- Avaliar melhorias visuais opcionais (cores, indentação mais elaborada) sem perder a simplicidade do ASCII.
- Complementar a documentação final descrevendo o fluxo completo com capturas de tela das simulações.
