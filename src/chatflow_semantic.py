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
    python src/chatflow_semantic.py   # e pressione ENTER para usar exemplos/from_rules.json
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple, Optional
import json
import sys
import os

# ------------------------------------------------------------
# Classes de dados
# ------------------------------------------------------------

@dataclass
class SemanticIssue:
    kind: str   # 'ERROR' ou 'WARN'
    message: str
    where: Optional[str] = None

@dataclass
class SymbolTable:
    states: Set[str] = field(default_factory=set)
    intents: Set[str] = field(default_factory=set)
    transitions: List[Tuple[str, str, str]] = field(default_factory=list)  # (from_state, intent, to_state)


# ------------------------------------------------------------
# Analisador semântico
# ------------------------------------------------------------

class ChatFlowSemanticAnalyzer:
    def __init__(self, ir: Dict):
        self.ir = ir
        self.table = SymbolTable()
        self.issues: List[SemanticIssue] = []

    # 1) Tabela de símbolos
    def build_symbol_table(self):
        states = self.ir.get("states", {}) or {}
        for st in states.keys():
            self.table.states.add(st)
        for intent in self.ir.get("intents", []) or []:
            self.table.intents.add(intent)
        for st_name, st_def in states.items():
            for tr in (st_def.get("on", []) or []):
                intent = tr.get("intent")
                to = tr.get("to")
                self.table.transitions.append((st_name, intent, to))

    # 2) Verificações
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

    # 3) Estados órfãos
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

    def analyze(self):
        self.build_symbol_table()
        self.check_undefined_states_in_transitions()
        self.check_undefined_intents_in_transitions()
        self.check_orphan_states()
        return self.table, self.issues


# ------------------------------------------------------------
# Relatório
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
        print("Nenhum problema encontrado ")
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
        print(" Nenhum estado inicial definido.")
        return
    states = ir.get("states", {}) or {}
    current = start

    print(f"Estado inicial: {current}")
    while True:
        st = states.get(current, {}) or {}
        options = st.get("on", []) or []

        # Se houver mensagem de resposta no estado, exiba (se existir no JSON)
        reply = st.get("respond")
        if reply:
            print(f"[{current}] RESPONDER: {reply}")

        if not options:
            print(f" Estado '{current}' não possui transições. Fim do fluxo.")
            break

        print("\nOpções disponíveis:")
        for i, opt in enumerate(options, start=1):
            print(f"  {i}) {opt.get('intent')} → {opt.get('to')}")

        user = input("Digite a intenção (ou ENTER para encerrar): ").strip().lower()
        if user == "":
            print("Encerrando simulação.")
            break

        moved = False
        for tr in options:
            if str(tr.get("intent", "")).lower() == user:
                print(f"[{current}] --[{user}]--> {tr.get('to')}")
                current = tr.get("to")
                moved = True
                break
        if not moved:
            print(f" Intenção '{user}' não é válida neste estado.")


# ------------------------------------------------------------
# Utilitários de caminho e main
# ------------------------------------------------------------

def resolve_default_json_path(default_rel="exemplos/from_rules.json") -> str:
    """
    Resolve o caminho padrão relativo à raiz do projeto,
    independente de onde o script esteja sendo executado.
    """
    # pasta do arquivo atual (src/)
    here = os.path.dirname(os.path.abspath(__file__))
    # sobe um nível (raiz do projeto)
    root = os.path.abspath(os.path.join(here, os.pardir))
    return os.path.join(root, default_rel.replace("/", os.sep))

def main():
    print("=== ANALISADOR SEMÂNTICO CHATFLOW ===")

    # 1) Caminho do JSON via argumento, se houver
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # 2) Pergunta ao usuário; ENTER usa o exemplo padrão
        suggested = resolve_default_json_path()
        rel_hint = "exemplos/from_rules.json"
        prompt = f"Digite o caminho do arquivo JSON (ENTER para usar {rel_hint}): "
        entered = input(prompt).strip()
        path = entered if entered else suggested

    try:
        with open(path, "r", encoding="utf-8") as f:
            ir = json.load(f)
    except FileNotFoundError:
        print(f" Arquivo não encontrado: {path}")
        # dica amiga se tentou usar o padrão mas não existe
        default_try = resolve_default_json_path()
        if path == default_try:
            print("Dica: verifique se a pasta 'exemplos/' está na raiz do projeto e contém 'from_rules.json'.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f" Erro ao ler o JSON ({path}): {e}")
        sys.exit(1)

    analyzer = ChatFlowSemanticAnalyzer(ir)
    table, issues = analyzer.analyze()
    print_report(table, issues)

    # Se não houver erros, oferece simulação
    if not any(i.kind.upper() == "ERROR" for i in issues):
        resp = input("\nDeseja simular o fluxo? (s/N): ").strip().lower()
        if resp == "s":
            simulate_chatflow(ir)
    else:
        print("\n Erros foram detectados — simulação desativada.")


if __name__ == "__main__":
    main()
