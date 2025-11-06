<<<<<<< HEAD
# Projeto

## 🔁 Regras ChatFlow → IR (JSON) + 3 fluxos

Este projeto inclui um **tradutor de regras ChatFlow (DSL mínima)** para a **estrutura intermediária (IR) em JSON** consumida pelo analisador semântico.

### Como usar
1. Edite suas regras em `exemplos/chatflow_rules_example.cf`:
   ```
   start_state: Inicio
   intents: saudacao, ajuda, sair, erro

   state Inicio:
     on saudacao -> Saudacao
     on erro -> Fim

   state Saudacao:
     on ajuda -> Ajuda
     on sair -> Fim

   state Ajuda:
     on sair -> Fim

   state Fim:
     respond "Até mais!"
   ```
2. Gere o JSON:
   ```bash
   python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf exemplos/from_rules.json
   ```
3. Rode o analisador com o JSON gerado:
   ```bash
   python src/chatflow_semantic.py exemplos/from_rules.json
   ```

### 3 Fluxos completos
A documentação `docs/fluxos.md` apresenta **3 fluxos de diálogo completos** correspondentes às regras acima.


### ▶ Simulador de fluxos (opcional)
Você pode simular uma sequência de intents sobre a IR em JSON:

```bash
# gerar IR a partir das regras
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf exemplos/from_rules.json

# simular 3 fluxos diferentes
python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo1.txt
python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo2.txt
python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo3.txt

# ou passar intents inline
python tools/simulate_chatflow.py exemplos/from_rules.json --intents saudacao ajuda sair
```
=======
# Compiladores_E01 Grupo02

Repositório do **Projeto Compiladores — Unidade II** (Grupo 02).  
**Semana 01**: *Análise Semântica e Tabela de Símbolos (ChatFlow DSL)*.

## 🎯 Objetivo
Implementar a fase da **Semana 01**:
- Verificar **variáveis/intenções/transições válidas**;
- Criar **Tabela de Símbolos** (estados, intenções, transições);
- Detectar **inconsistências** (*transições inexistentes* e *estados órfãos*).

## 🧰 Linguagem e ferramentas utilizadas
- **Linguagem:** Python 3.10+
- **Ferramentas:** padrão da biblioteca Python (sem dependências externas).

## ▶️ Instruções de execução
Clonar o repositório e executar:

```bash
python src/chatflow_semantic.py exemplos/valid.json
python src/chatflow_semantic.py exemplos/invalid.json
```

Saídas de exemplo em [`/exemplos/Exemplo_Saida.txt`](exemplos/Exemplo_Saida.txt).

## 👤 Responsabilidades de cada integrante
- **Ramon Costa Da Guia** — Semântica, Tabela de Símbolos, Integração inicial.
- **Thiago Estombelo Llapa** — Definição de casos de teste e exemplos.
- **Luiz Felipe de Araujo Menezes** — Organização do repositório e documentação.

> Nota: responsabilidades podem ser atualizadas a cada semana conforme evolução do projeto.

## 📂 Estrutura do repositório
```
Compiladores_E01 Grupo02/
├── src/
│   └── chatflow_semantic.py        # Semana 01 — semântica + tabela de símbolos
├── docs/
│   └── Semana01_Documentacao.pdf   # Documentação parcial (Semana 01)
├── exemplos/
│   ├── valid.json                  # Exemplo válido
│   ├── invalid.json                # Exemplo com erros
│   └── Exemplo_Saida.txt          # Saídas de execução (demonstração)
├── demo/
│   └── README.md                   # Instruções p/ gravação do vídeo (para a semana final)
└── README.md
```

## 📸 Exemplos de saída
Veja o arquivo [`/exemplos/Exemplo_Saida.txt`](exemplos/Exemplo_Saida.txt) com as execuções dos casos **válido** e **com erros**.

## 📹 Demo (para o final)
A pasta [`/demo`](demo/) conterá um **vídeo `.mp4` (máx. 5 min)** com a execução básica do sistema.  
Para a Semana 01, apenas mantemos as instruções.
>>>>>>> 7f9cb31ea7811f2745af89877d1985be8c919a84
