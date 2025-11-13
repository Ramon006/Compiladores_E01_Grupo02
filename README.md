<h1 align="center">💬 ChatFlow</h1>
<p align="center"><strong>Linguagem de Diálogo para Chatbots — Grupo 02</strong></p>

-----------------------------------------------------------------------------------------------------------------
<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/Licença-MIT-green.svg"></a>
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg">
  <img src="https://img.shields.io/badge/Feito%20por-Grupo%2002-orange.svg">
</p>

-----------------------------------------------------------------------------------------------------------------

Este projeto apresenta a **ChatFlow**, uma DSL (Domain-Specific Language) mínima desenvolvida para **modelar fluxos de diálogo** e traduzi-los para uma **Representação Intermediária (IR)** em formato **JSON**, utilizada por analisadores e simuladores.  
Inclui também um **simulador funcional** e **três fluxos de exemplo** totalmente reprodutíveis.


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

## 👥 Equipe de Desenvolvimento(exemplo)

| Nome | GitHub | Principais Responsabilidades |
|------|---------|------------------------------|
| **Ramon** | [@Ramon006](https://github.com/Ramon006) | Coordenação geral, desenvolvimento do simulador |
| **Integrante 2** | [@user2](https://github.com/user2) | Implementação da DSL e do Parser |
| **Integrante 3** | [@ThiagoEstombelo](https://github.com/ThiagoEstombelo) | IR (Intermediate Representation) e validações semânticas |


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
