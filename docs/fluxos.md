# Fluxos de Diálogo — Demonstração (3 completos)

Este documento demonstra **três fluxos completos** a partir das regras da linguagem ChatFlow
utilizadas no projeto. Todos os fluxos são compatíveis com a IR (JSON) usada pelos módulos:

- `tools/chatflow_to_json.py`
- `src/chatflow_semantic.py`
- `tools/simulate_chatflow.py`
- `tools/visualize_chatflow.py`

Os estados principais utilizados nos exemplos são:

- `Inicio`
- `Saudacao`
- `Ajuda`
- `Fim`

As intents utilizadas:

- `saudacao`
- `ajuda`
- `sair`
- `erro`


---

## Fluxo 1 — saudacao → ajuda → sair (Fluxo de atendimento completo)

### Descrição em texto

1. O diálogo começa no estado **`Inicio`**.  
2. O usuário envia a intent **`saudacao`**, e o fluxo segue para o estado **`Saudacao`**.  
3. No estado **`Saudacao`**, o bot responde com uma mensagem de boas-vindas e o usuário pode pedir **`ajuda`**.  
4. Ao enviar a intent **`ajuda`**, o fluxo muda para o estado **`Ajuda`**, onde o bot lista opções.  
5. A partir do estado **`Ajuda`**, o usuário envia a intent **`sair`**, e o fluxo é encerrado no estado **`Fim`**.

### Diagrama ASCII

```text
Fluxo 1 — saudacao → ajuda → sair

[Inicio]
  |--[saudacao]--> Saudacao

[Saudacao]
  responde: "Olá! Como posso ajudar?"
  |--[ajuda]--> Ajuda

[Ajuda]
  responde: "Aqui estão algumas opções..."
  |--[sair]--> Fim

[Fim] (fim)
  responde: "Até mais!"
