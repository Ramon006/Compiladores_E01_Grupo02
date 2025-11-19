
# 🧠 Compiladores — ChatFlow Compiler

**Grupo 02 — Disciplina de Compiladores**

Este repositório contém a implementação completa de um **compilador para a linguagem ChatFlow**, uma DSL criada para definir sistemas de diálogo baseados em estados, intenções e transições.  
O compilador implementa: análise léxica, sintática simplificada, análise semântica, geração de JSON (IR), simulação interativa e visualização ASCII.

---

# 📌 Objetivo do Projeto

- Interpretar regras de diálogo escritas em ChatFlow  
- Identificar erros sintáticos e semânticos  
- Gerar código intermediário JSON  
- Simular a execução de diálogos reais  
- Visualizar fluxos em ASCII  
- Validar transições, intenções e estados órfãos  

---

# 🗂 Estrutura do Repositório

```
Compiladores_E01_Grupo02/
│
├── src/
│   ├── chatflow_semantic.py
│
├── tools/
│   ├── chatflow_to_json.py
│   ├── simulate_chatflow.py
│   ├── visualize_chatflow.py
│
├── exemplos/
│   ├── chatflow_rules_example.cf
│   ├── valid.json
│   ├── invalid.json
│   ├── fluxo1.txt, fluxo2.txt, fluxo3.txt
│   ├── from_rules.json
│
├── docs/
│   ├── fluxos.md
│   ├── semanal-01.md
│   ├── semanal-02.md
│   ├── semanal-03.md
│   ├── final.pdf
│
├── tests/
│   ├── test_invalid_state.py
│
├── schema/
│   ├── ir.schema.json
│
├── demo/
│   ├── demo.mp4
│
└── README.md
```

---

# 🐍 Requisitos

- **Python 3.10+**
- Biblioteca `jsonschema`
- Biblioteca `rich` (opcional)

Instalação:

```bash
pip install -r requirements.txt
```

---

# 🚀 Como Executar o Projeto (GitHub Codespaces)

Este projeto foi totalmente testado no **GitHub Codespaces**.

---

# 🧰 Abrindo o Terminal no Codespaces

1. Clique no **menu de três barras (☰)** no canto superior esquerdo  
2. Vá em:

```
Terminal → New Terminal
```

3. O terminal abrirá na parte inferior em:

```
/workspaces/Compiladores_E01_Grupo02
```

---

# ▶️ 1. Converter ChatFlow (.cf) para JSON

O conversor usa **dois argumentos**, sem `-o`:

```bash
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf fluxo.json
```

Confirme o arquivo criado:

```bash
ls
```

---

# ▶️ 2. Executar o Analisador Semântico

```bash
python src/chatflow_semantic.py
```

Quando solicitado:

- Pressione **ENTER** para usar `exemplos/from_rules.json`,  
ou  
- Digite:

```
fluxo.json
```

---

# ▶️ 3. Simulação Interativa

```bash
python src/chatflow_semantic.py fluxo.json
```

Digite intenções conforme o fluxo:

```
saudacao
ajuda
sair
```

---

# ▶️ 4. Visualização ASCII

```bash
python tools/visualize_chatflow.py fluxo.json
```

Exemplo de saída:

```
[Inicio] --saudacao--> [Saudacao]
[Saudacao] --ajuda--> [Ajuda]
[Ajuda] --sair--> [Fim]
```

---

# ▶️ 5. Pipeline Completo

```bash
python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf fluxo.json
python src/chatflow_semantic.py fluxo.json
python tools/simulate_chatflow.py fluxo.json
python tools/visualize_chatflow.py fluxo.json
```

---



# 🧩 Exemplos de Fluxos (docs/fluxos.md)

O arquivo possui:

- 3 fluxos completos  
- Diagramas ASCII  
- Versões JSON  
- Descrição detalhada  
- Erros e caminhos alternativos  

---

# 👥 Integrantes

| Nome | Função |
|------|--------|
| **Ramon Costa da Guia** | Desenvolvimento principal, análise semântica, integração e documentação |
| **Luiz Felipe de Araujo Menezes** | Ferramentas, testes e simulação |
| **Thiago Estombelo Llapa** | Conversor ChatFlow → JSON, fluxos e validação |

---

# 📝 Entregas da Disciplina

| Entrega | Status |
|---------|--------|
| Configuração do Repositório | ✔ |
| Documentos Semanais | ✔ |
| Compilador Completo | ✔ |
| Visualização ASCII | ✔ |
| Simulador Interativo | ✔ |
| Documentação Final | ✔ |
| Vídeo Demo | 🔄 Em produção |

---

# 🎥 Demo

Disponível em:

```
/demo/demo.mp4
```

---

# ✔ Conclusão

Este repositório entrega um compilador totalmente funcional para a linguagem ChatFlow, incluindo todas as etapas essenciais: conversão, validação, simulação e visualização. Projeto completo e pronto para avaliação.

---

# 📫 Contato

**ramon.guia@souunit.com.br**  
**luiz.felipe04@souunit.com.br**  
**thiago.estombelo@souunit.com.br**
