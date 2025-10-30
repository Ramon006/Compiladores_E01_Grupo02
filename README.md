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
- **Luiz Felipe** — Organização do repositório e documentação.

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
