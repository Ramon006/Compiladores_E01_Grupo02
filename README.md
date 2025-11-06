# Linguagem de Diálogo para Chatbots — Grupo 02

Este repositório implementa uma DSL mínima (ChatFlow) para modelagem de diálogos e sua tradução para uma **Estrutura Intermediária (IR)** consumível por analisadores (JSON). Inclui simulador e exemplos com **3 fluxos completos**.

## 📁 Estrutura
```
/src        # Código-fonte (Python) — conversores e simulador
/docs       # Documentação semanal + versão final (final.pdf)
/exemplos   # Regras de exemplo (.cf) e scripts de intents
/tools      # Ferramentas utilitárias (cópia de referência)
/schema     # JSON Schema do IR (opcional)
/tests      # Testes de exemplo (negativos/borda)
/demo       # Vídeo demo (demo.mp4) — até 5 min
README.md
```
> Observação: mantemos `tools/` como referência e duplicamos os conversores em `/src` para atender ao requisito de código em `/src`.

## 🛠️ Ferramentas
- Python 3.11+
- (Opcional) `make` para atalhos de build/demo/test
- (Opcional) Git LFS para `demo/demo.mp4` caso >100MB

## ▶️ Como executar (exemplo em Python)
### 1) Gerar IR (JSON) a partir da DSL:
```bash
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf exemplos/from_rules.json
# ou via src/ (cópia do mesmo script)
python src/chatflow_to_json.py exemplos/chatflow_rules_example.cf exemplos/from_rules.json
```

### 2) Simular 3 fluxos
```bash
python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo1.txt
python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo2.txt
python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo3.txt

# também é possível inline:
python tools/simulate_chatflow.py exemplos/from_rules.json --intents saudacao ajuda sair
```

### 3) (Opcional) Pseudo‑código a partir da IR
```bash
python tools/chatflow_to_pseudocode.py exemplos/from_rules.json
```

## ✅ Critérios atendidos
- Tradução ChatFlow → **IR (JSON)** e pseudo‑código textual opcional
- **3 fluxos completos** simulados e reproduzíveis
- **/src**, **/docs**, **/exemplos**, **/demo**, **README.md** no padrão
- **Docs semanais** e versão final (`docs/final.pdf` placeholder)
- Commits de acompanhamento (participação individual)

## 👥 Responsáveis (exemplo)
| Integrante | GitHub | Responsabilidades |
|-----------|--------|-------------------|
| Ramon     | @Ramon006 | Coordenação, simulador |
| Integrante 2 | @user2   | DSL/Parser |
| Integrante 3 | @user3   | IR/Validações |

## 🧪 Testes
Executar testes (exemplo negativo em `tests/`):
```bash
python -m unittest discover -s tests -p "*.py"
```

## 🎬 Demo
Adicionar `demo/demo.mp4` (até 5 min). Se o arquivo ficar grande, use Git LFS:
```bash
git lfs install
git lfs track "*.mp4"
git add .gitattributes demo/demo.mp4
git commit -m "Add demo.mp4 via LFS"
git push
```

## 📜 Licença
MIT (ou a definida pela disciplina).
