#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChatFlow rules -> IR JSON
Sintaxe suportada:
- start_state: <EstadoInicial>
- intents: a,b,c
- state <Nome>:
    respond "Texto opcional"
    on <intent> -> <Destino>
"""
import re, json, sys, argparse
from pathlib import Path

def parse_rules(text: str):
    lines = [ln.rstrip() for ln in text.splitlines()]
    start_state = None
    intents = []
    states = {}
    cur = None

    rgx = {
        "start": re.compile(r'^\s*start_state\s*:\s*([A-Za-z0-9_]+)\s*$'),
        "intents": re.compile(r'^\s*intents\s*:\s*(.+?)\s*$'),
        "state_hdr": re.compile(r'^\s*state\s+([A-Za-z0-9_]+)\s*:\s*$'),
        "respond": re.compile(r'^\s*respond\s+"(.*)"\s*$'),
        "on": re.compile(r'^\s*on\s+([A-Za-z0-9_]+)\s*->\s*([A-Za-z0-9_]+)\s*$'),
    }

    for ln in lines:
        if not ln.strip():
            continue
        m = rgx["start"].match(ln)
        if m:
            start_state = m.group(1)
            continue
        m = rgx["intents"].match(ln)
        if m:
            intents = [x.strip() for x in m.group(1).split(",") if x.strip()]
            continue
        m = rgx["state_hdr"].match(ln)
        if m:
            cur = m.group(1)
            states.setdefault(cur, {})
            continue
        if cur:
            m = rgx["respond"].match(ln)
            if m:
                states[cur]["respond"] = m.group(1)
                continue
            m = rgx["on"].match(ln)
            if m:
                intent, to = m.group(1), m.group(2)
                states[cur].setdefault("on", []).append({"intent": intent, "to": to})
                continue

    if not start_state:
        raise ValueError("start_state não definido.")
    return {
        "start_state": start_state,
        "states": states,
        **({"intents": intents} if intents else {})
    }

def main():
    ap = argparse.ArgumentParser(description="Traduz regras ChatFlow (DSL) para IR JSON.")
    ap.add_argument("rules", help="Arquivo de regras (.cf)")
    ap.add_argument("out", help="Arquivo de saída JSON")
    args = ap.parse_args()

    text = Path(args.rules).read_text(encoding="utf-8")
    ir = parse_rules(text)
    Path(args.out).write_text(json.dumps(ir, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] Gerado: {args.out}")

if __name__ == "__main__":
    main()
