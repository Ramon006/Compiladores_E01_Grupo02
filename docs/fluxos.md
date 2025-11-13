# Fluxos de Diálogo --- Demonstração Oficial (3 Fluxos Completos)

Este documento apresenta **três fluxos de diálogo completos**, seguindo
o modelo da linguagem ChatFlow implementada neste projeto.

Cada fluxo contém:

-   ✔ Descrição em texto\
-   ✔ Diagrama ASCII\
-   ✔ Representação em JSON (IR) compatível com o compilador\
-   ✔ Estados e intents usados no projeto real

Os fluxos abaixo são usados para demonstrar o funcionamento completo das
fases:

-   Tradução de regras → JSON\
-   Validação semântica\
-   Execução interativa\
-   Visualização ASCII

------------------------------------------------------------------------

# 🔵 Fluxo 1 --- `saudacao → ajuda → sair` (Fluxo de atendimento completo)

## Descrição do fluxo

1.  O diálogo começa no estado inicial **`Inicio`**.\
2.  O usuário envia a intent **`saudacao`**, indo para o estado
    **`Saudacao`**.\
3.  O bot responde "Olá! Como posso ajudar?".\
4.  O usuário então envia **`ajuda`**, indo para o estado **`Ajuda`**.\
5.  O bot lista opções disponíveis.\
6.  O usuário envia **`sair`**, levando ao estado **`Fim`**.\
7.  O bot encerra com "Até mais!".

------------------------------------------------------------------------

## Diagrama ASCII

``` text
Fluxo 1 — saudacao → ajuda → sair

[Inicio]
  |--[saudacao]--> Saudacao
  |--[erro]--> Fim

[Saudacao]
  responde: "Olá! Como posso ajudar?"
  |--[ajuda]--> Ajuda
  |--[sair]--> Fim

[Ajuda]
  responde: "Aqui estão algumas opções..."
  |--[sair]--> Fim

[Fim] (fim)
  responde: "Até mais!"
```

------------------------------------------------------------------------

## JSON (IR compatível com o compilador)

``` json
{
  "start_state": "Inicio",
  "intents": ["saudacao", "ajuda", "sair", "erro"],
  "states": {
    "Inicio": {
      "on": [
        { "intent": "saudacao", "to": "Saudacao" },
        { "intent": "erro",      "to": "Fim" }
      ]
    },
    "Saudacao": {
      "respond": "Olá! Como posso ajudar?",
      "on": [
        { "intent": "ajuda", "to": "Ajuda" },
        { "intent": "sair",  "to": "Fim" }
      ]
    },
    "Ajuda": {
      "respond": "Aqui estão algumas opções...",
      "on": [
        { "intent": "sair", "to": "Fim" }
      ]
    },
    "Fim": {
      "respond": "Até mais!"
    }
  }
}
```

------------------------------------------------------------------------

# 🟠 Fluxo 2 --- `erro → fim` (Encerramento imediato)

## Descrição do fluxo

Este fluxo representa um caso de **tratamento de erro**:

1.  O diálogo começa em **`Inicio`**.\
2.  O usuário envia a intent **`erro`** (entrada inválida).\
3.  O fluxo vai diretamente para **`Fim`**.\
4.  A conversa é encerrada.

------------------------------------------------------------------------

## Diagrama ASCII

``` text
Fluxo 2 — erro direto para fim

[Inicio]
  |--[erro]--> Fim

[Fim] (fim)
  responde: "Até mais!"
```

------------------------------------------------------------------------

## JSON (trecho específico do fluxo)

``` json
{
  "start_state": "Inicio",
  "states": {
    "Inicio": {
      "on": [
        { "intent": "erro", "to": "Fim" }
      ]
    },
    "Fim": {
      "respond": "Até mais!"
    }
  }
}
```

------------------------------------------------------------------------

# 🟢 Fluxo 3 --- `saudacao → sair` (Atendimento rápido)

## Descrição do fluxo

Um caminho mais curto:

1.  O usuário envia **`saudacao`**.\
2.  O fluxo vai para **`Saudacao`**.\
3.  O bot responde normalmente.\
4.  O usuário escolhe **`sair`** imediatamente.\
5.  O fluxo vai direto para **`Fim`**.

------------------------------------------------------------------------

## Diagrama ASCII

``` text
Fluxo 3 — saudacao → sair

[Inicio]
  |--[saudacao]--> Saudacao

[Saudacao]
  responde: "Olá! Como posso ajudar?"
  |--[sair]--> Fim

[Fim] (fim)
  responde: "Até mais!"
```

------------------------------------------------------------------------

## JSON (Fluxo 3 completo dentro da mesma definição)

``` json
{
  "start_state": "Inicio",
  "states": {
    "Inicio": {
      "on": [
        { "intent": "saudacao", "to": "Saudacao" },
        { "intent": "erro",      "to": "Fim" }
      ]
    },
    "Saudacao": {
      "respond": "Olá! Como posso ajudar?",
      "on": [
        { "intent": "sair", "to": "Fim" }
      ]
    },
    "Fim": {
      "respond": "Até mais!"
    }
  }
}
```

------------------------------------------------------------------------

# ✔ Conclusão

Este documento atende aos requisitos:

-   "demonstrar **3 fluxos de diálogo completos**"
-   incluir exemplos estruturados
-   apresentar representação JSON compatível com o compilador
-   diagrama ASCII simples
-   descrição clara
