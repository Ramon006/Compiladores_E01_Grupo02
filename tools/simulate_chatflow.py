#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulador de ChatFlow a partir da IR (JSON).
Uso:
  python tools/simulate_chatflow.py <ir.json> --intents saudacao ajuda sair
  # ou
  python tools/simulate_chatflow.py <ir.json> --script exemplos/roteiro.txt

Saída:
- Caminho percorrido: estados, intents e respostas (se houver).
- Indica erros quando um intent não existe no estado atual.
"""
import argparse, json, sys
from pathlib import Path

def simulate(ir, intents_seq):
    states = ir.get("states", {})
    cur = ir.get("start_state")
    if cur is None:
        raise ValueError("IR inválida: start_state ausente.")
    path = []
    for it in intents_seq:
        st = states.get(cur, {})
        transitions = st.get("on", [])
        # resposta do estado atual (se houver)
        if "respond" in st:
            path.append({"state": cur, "respond": st["respond"]})
        # procura transição
        next_state = None
        for tr in transitions:
            if tr.get("intent") == it:
                next_state = tr.get("to")
                break
        if next_state is None:
            return path, f"Erro: no estado '{cur}' não existe transição para intent '{it}'."
        path.append({"state": cur, "intent": it, "to": next_state})
        cur = next_state
    # resposta final (se houver)
    st = states.get(cur, {})
    if "respond" in st:
        path.append({"state": cur, "respond": st["respond"]})
    return path, None

def main():
    ap = argparse.ArgumentParser(description="Simulador de fluxos de diálogo a partir da IR (JSON).")
    ap.add_argument("ir_json", help="Arquivo JSON com a IR (ex.: exemplos/from_rules.json)")
    ap.add_argument("--intents", nargs="*", default=None, help="Sequência de intents (ex.: saudacao ajuda sair)")
    ap.add_argument("--script", type=str, default=None, help="Arquivo com intents, uma por linha.")
    args = ap.parse_args()

    ir = json.loads(Path(args.ir_json).read_text(encoding="utf-8"))

    if args.script:
        intents_seq = [ln.strip() for ln in Path(args.script).read_text(encoding="utf-8").splitlines() if ln.strip()]
    else:
        intents_seq = args.intents or []

    path, err = simulate(ir, intents_seq)
    print("=== SIMULAÇÃO ===")
    print(f"start_state: {ir.get('start_state')}")
    print("sequência:", " ".join(intents_seq) if intents_seq else "(vazia)")
    print("\n--- Caminho ---")
    for step in path:
        if "respond" in step and "intent" not in step:
            print(f"[{step['state']}] RESPONDER: {step['respond']}")
        elif "intent" in step:
            print(f"[{step['state']}] --[{step['intent']}]--> {step['to']}")
    if err:
        print("\n---")
        print(err)
        sys.exit(2)
    else:
        print("\nConcluído sem erros.")
        sys.exit(0)

if __name__ == "__main__":
    main()
