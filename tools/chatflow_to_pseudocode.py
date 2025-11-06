#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera pseudo-código textual a partir da IR em JSON."""
import json, sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Uso: python tools/chatflow_to_pseudocode.py <arquivo_ir.json>")
        sys.exit(1)
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    print("Pseudo-código ChatFlow:")
    print(f"Início em {data['start_state']}")
    for sname, sdef in data["states"].items():
        print(f"\nEstado {sname}:")
        if "respond" in sdef:
            print(f"  Responde: {sdef['respond']}")
        for t in sdef.get("on", []):
            print(f"  se {t['intent']} -> {t['to']}")
if __name__ == "__main__":
    main()
