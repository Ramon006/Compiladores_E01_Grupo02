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
