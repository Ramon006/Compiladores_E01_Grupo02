# 🧠 Compiladores --- ChatFlow Compiler

**Grupo 02 --- Disciplina de Compiladores**

Este repositório contém a implementação completa de um **compilador para
a linguagem ChatFlow**, uma DSL criada para definir sistemas de diálogo
baseados em estados, intenções e transições.\
O compilador possui todas as fases essenciais --- análise léxica,
sintática simplificada, análise semântica, geração de código
intermediário (JSON), simulação interativa e visualização ASCII.

------------------------------------------------------------------------

# 📌 Objetivo do Projeto

Desenvolver um compilador funcional capaz de:

-   Interpretar regras de diálogo escritas em ChatFlow\
-   Identificar erros sintáticos e semânticos\
-   Gerar código intermediário (IR) em formato JSON\
-   Simular a execução de um diálogo real\
-   Exibir fluxogramas ASCII mostrando o fluxo do diálogo\
-   Validar intenções, estados, transições e detectar estados órfãos

Este projeto atende integralmente os requisitos da disciplina.

------------------------------------------------------------------------

# 🗂 Estrutura do Repositório

    Compiladores_E01_Grupo02/
    │
    ├── src/                     # Código-fonte principal (analisador semântico)
    │   ├── chatflow_semantic.py
    │
    ├── tools/                   # Ferramentas do compilador
    │   ├── chatflow_to_json.py
    │   ├── simulate_chatflow.py
    │   ├── visualize_chatflow.py
    │
    ├── exemplos/                # Exemplos para teste
    │   ├── chatflow_rules_example.cf
    │   ├── valid.json
    │   ├── invalid.json
    │   ├── fluxo1.txt, fluxo2.txt, fluxo3.txt
    │
    ├── docs/                    # Documentação parcial e final
    │   ├── fluxos.md
    │   ├── semanal-01.md
    │   ├── semanal-02.md
    │   ├── semanal-03.md
    │   ├── final.pdf
    │
    ├── tests/                   # Testes automatizados
    │   ├── test_invalid_state.py
    │
    ├── schema/                  # Esquemas JSON usados na validação
    │   ├── ir.schema.json
    │
    ├── demo/                    # Vídeo demonstrativo (quando entregue)
    │   ├── demo.mp4
    │
    └── README.md                # Este arquivo

------------------------------------------------------------------------

# 🐍 Requisitos

-   **Python 3.10+** (obrigatório devido ao uso de `match/case`)
-   Biblioteca `jsonschema`\
-   Biblioteca `rich` (opcional para melhor visualização)

Instale tudo com:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 🚀 Como Executar o Projeto

O compilador possui três módulos principais:

1.  **Conversor ChatFlow → JSON**\
2.  **Analisador Semântico**\
3.  **Simulador Interativo de Diálogo**\
4.  **Visualizador ASCII**

Todos estão na pasta `tools/` e `src/`.

------------------------------------------------------------------------

# ▶️ 1. Converter Regras ChatFlow para JSON

Exemplo:

``` bash
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf
```

Salvar a saída em arquivo:

``` bash
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf -o saida.json
```

------------------------------------------------------------------------

# ▶️ 2. Executar o Analisador Semântico

``` bash
python src/chatflow_semantic.py
```

Quando pedir o caminho, você pode:

✔ pressionar **ENTER** para usar `exemplos/from_rules.json`\
ou\
✔ digitar outro arquivo:

``` bash
exemplos/valid.json
```

------------------------------------------------------------------------

# ▶️ 3. Simulação Interativa do Fluxo

``` bash
python tools/simulate_chatflow.py exemplos/valid.json
```

Digite as intenções no terminal:

    saudacao
    ajuda
    sair

O simulador segue as transições definidas no JSON.

------------------------------------------------------------------------

# ▶️ 4. Visualização ASCII do Fluxo

``` bash
python tools/visualize_chatflow.py exemplos/valid.json
```

Saída esperada (exemplo):

    [Inicio] --saudacao--> [Saudacao]
    [Saudacao] --ajuda--> [Ajuda]
    [Ajuda] --sair--> [Fim]

------------------------------------------------------------------------

# ▶️ 5. Pipeline Completo (Compilador Inteiro)

``` bash
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf -o fluxo.json
python src/chatflow_semantic.py fluxo.json
python tools/simulate_chatflow.py fluxo.json
python tools/visualize_chatflow.py fluxo.json
```

------------------------------------------------------------------------

# 🧪 Testes Automatizados

Executar todos os testes:

``` bash
pytest -v
```

Ou um teste específico:

``` bash
python tests/test_invalid_state.py
```

------------------------------------------------------------------------

# 🧩 Exemplos de Fluxos (documentados em `docs/fluxos.md`)

O arquivo `docs/fluxos.md` contém:

-   3 fluxos completos\
-   Diagramas ASCII\
-   Representação JSON\
-   Descrição detalhada\
-   Caminhos alternativos e erros

Esse documento é parte essencial da entrega.

------------------------------------------------------------------------

# 👥 Integrantes do Grupo

  -----------------------------------------------------------------------
  Nome                                     Função / Responsabilidades
  ---------------------------------------- ------------------------------
  **Ramon Costa da Guia**                  Desenvolvimento principal,
                                           análise semântica, integração
                                           geral, documentação.

  **Luiz Felipe de Araujo Menezes**        Implementação de ferramentas
                                           (`tools`), testes e simulação.

  Thiago Estombelo Llapa               Conversão ChatFlow → JSON,
                                           estrutura de fluxos e
                                           validação.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 📝 Entregas da Disciplina

  Entrega                        Status
  ------------------------------ ----------------
  Configuração do Repositório    ✔ Concluída
  Documento Semanal (Semana 1)   ✔
  Documento Semanal (Semana 2)   ✔
  Documento Semanal (Semana 3)   ✔
  Compilador Completo            ✔
  Visualização ASCII             ✔
  Simulador Interativo           ✔
  Documentação Final             ✔
  Vídeo Demo (até 5 minutos)     🔄 Em produção

------------------------------------------------------------------------

# 🎥 Demo (quando concluída)

O vídeo demonstrativo ficará na pasta:

    /demo/demo.mp4

------------------------------------------------------------------------

# ✔ Conclusão

Este repositório contém um compilador totalmente funcional para a
linguagem ChatFlow, com todas as fases implementadas, testes
automáticos, documentação parcial e final, e demonstrações práticas
exigidas pela disciplina.

O projeto está pronto para avaliação.

------------------------------------------------------------------------

# 📫 Contato

**ramon.guia@souunit.com.br**
