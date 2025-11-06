"""
ChatFlow — Semana 01: Análise Semântica e Tabela de Símbolos (Python)
Grupo 02 — Unidade II
Implementa:
- Verificação de variáveis, intenções e transições válidas
- Criação da Tabela de Símbolos
- Detecção de inconsistências (transições inexistentes, estados órfãos)
- Modo de simulação interativa (opcional)

Uso:
    python src/chatflow_semantic.py exemplos/from_rules.json
    ou apenas:
    python src/chatflow_semantic.py
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple, Optional
import json
import sys

# ------------------------------------------------------------
# Classes de dados
# ------------------------------------------------------------

@dataclass
class SemanticIssue:
    kind: str   # 'ERROR' or 'WARN'
    message: str
    where: Optional[str] = None

@dataclass
class SymbolTable:
    states: Set[str] = field(default_factory=set)
    intents: Set[str] = field(default_factory=set)
    transitions: List[Tuple[str, str, str]] = field(default_factory=list)  # (from_state, intent, to_state)


# ------------------------------------------------------------
# Classe principal do analisador semântico
# ------------------------------------------------------------

class ChatFlowSemanticAnalyzer:
    def __init__(self, ir: Dict):
        self.ir = ir
        self.table = SymbolTable()
        self.issues: List[SemanticIssue] = []

    # 1) Tabela de símbolos
    def build_symbol_table(self):
        states = self.ir.get("states", {})
        for st in states.keys():
            self.table.states.add(st)
        for intent in self.ir.get("intents", []):
            self.table.intents.add(intent)
        for st_name, st_def in states.items():
            for tr in st_def.get("on", []) or []:
                intent = tr.get("intent")
                to = tr.get("to")
                self.table.transitions.append((st_name, intent, to))

    # 2) Verificações de variáveis/intenções/transições
    def check_undefined_states_in_transitions(self):
        for frm, intent, to in self.table.transitions:
            if to not in self.table.states:
                self.issues.append(SemanticIssue(
                    "ERROR",
                    f"Transição '{frm}' --[{intent}]--> '{to}' aponta para estado inexistente.",
                    where=frm
                ))

    def check_undefined_intents_in_transitions(self):
        for frm, intent, to in self.table.transitions:
            if intent not in self.table.intents:
                self.issues.append(SemanticIssue(
                    "ERROR",
                    f"Intenção '{intent}' usada em '{frm}' não foi declarada.",
                    where=frm
                ))

    # 3) Inconsistências: estados órfãos
    def check_orphan_states(self):
        start = self.ir.get("start_state")
        if not start or start not in self.table.states:
            self.issues.append(SemanticIssue(
                "ERROR",
                "Estado inicial inválido ou ausente.",
                where=str(start)
            ))
            return

        graph: Dict[str, List[str]] = {s: [] for s in self.table.states}
        for frm, intent, to in self.table.transitions:
            graph[frm].append(to)

        visited: Set[str] = set()
        queue = [start]

        while queue:
            cur = queue.pop(0)
            if cur in visited:
                continue
            visited.add(cur)
            for nxt in graph.get(cur, []):
                if nxt not in visited:
                    queue.append(nxt)

        for s in self.table.states:
            if s not in visited:
                self.issues.append(SemanticIssue(
                    "WARN",
                    f"Estado '{s}' está órfão (inalcançável) a partir do estado inicial '{start}'.",
                    where=s
                ))

    # Executa todas as verificações
    def analyze(self):
        self.build_symbol_table()
        self.check_undefined_states_in_transitions()
        self.check_undefined_intents_in_transitions()
        self.check_orphan_states()
        return self.table, self.issues


# ------------------------------------------------------------
# Impressão do relatório
# ------------------------------------------------------------

def print_report(table: SymbolTable, issues: List[SemanticIssue]):
    print("=== TABELA DE SÍMBOLOS ===")
    print("Estados:", ", ".join(sorted(table.states)))
    print("Intenções:", ", ".join(sorted(table.intents)))
    print("Transições:")
    for a, b, c in table.transitions:
        print(f"  {a} --[{b}]--> {c}")

    print("\n=== PROBLEMAS DETECTADOS ===")
    if not issues:
        print("Nenhum problema encontrado ✅")
    else:
        for it in issues:
            where = f" (em {it.where})" if it.where else ""
            print(f"- {it.kind}: {it.message}{where}")


# ------------------------------------------------------------
# Simulação interativa
# ------------------------------------------------------------

def simulate_chatflow(ir: dict):
    print("\n=== SIMULAÇÃO INTERATIVA DO CHATFLOW ===")
    start = ir.get("start_state")
    if not start:
        print("⚠️ Nenhum estado inicial definido.")
        return
    states = ir.get("states", {})
    current = start

    print(f"Estado inicial: {current}")
    while True:
        state_info = states.get(current, {})
        options = state_info.get("on", [])
        if not options:
            print(f"🚩 Estado '{current}' não possui transições. Fim do fluxo.")
            break

        print("\nOpções disponíveis:")
        for i, opt in enumerate(options, start=1):
            print(f"  {i}) {opt['intent']} → {opt['to']}")

        user = input("Digite a intenção (ou 'sair' para encerrar): ").strip().lower()
        if user == "" or user == "sair":
            print("Encerrando simulação.")
            break

        found = False
        for tr in options:
            if tr["intent"].lower() == user:
                print(f"[{current}] --[{user}]--> {tr['to']}")
                current = tr["to"]
                found = True
                break
        if not found:
            print(f"❌ Intenção '{user}' não é válida neste estado.")


# ------------------------------------------------------------
# Função principal com input()
# ------------------------------------------------------------

def main():
    print("=== ANALISADOR SEMÂNTICO CHATFLOW ===")

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Digite o caminho do arquivo JSON de regras (ex: exemplos/from_rules.json): ").strip()

    if not path:
        print("❌ Nenhum arquivo informado. Encerrando.")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            ir = json.load(f)
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"⚠️ Erro ao ler o JSON: {e}")
        sys.exit(1)

    analyzer = ChatFlowSemanticAnalyzer(ir)
    table, issues = analyzer.analyze()
    print_report(table, issues)

    # Se não houver erros, oferece simulação
    if not any(i.kind == "ERROR" for i in issues):
        resp = input("\nDeseja simular o fluxo? (s/N): ").strip().lower()
        if resp == "s":
            simulate_chatflow(ir)
    else:
        print("\n⚠️ Erros foram detectados — simulação desativada.")


if __name__ == "__main__":
    main()
