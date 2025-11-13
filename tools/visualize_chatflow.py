#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera uma visualização simples em ASCII (fluxograma de estados)
a partir da IR em JSON da linguagem ChatFlow.

Uso:
  python tools/visualize_chatflow.py exemplos/from_rules.json
  python tools/visualize_chatflow.py exemplos/valid.json
"""

import json
import sys
from pathlib import Path


def build_ascii_flow(ir: dict) -> str:
    """Constroi uma representação textual simples do grafo de estados.

    Formato:

      Fluxograma ASCII do ChatFlow
      Início em: Inicio

      [Inicio]
        responde: "..." (opcional)
        |--[intent]--> ProximoEstado

      [OutroEstado] (fim)
        responde: "..."
    """
    lines = []

    start_state = ir.get("start_state") or "<desconhecido>"
    states = ir.get("states", {})

    lines.append("Fluxograma ASCII do ChatFlow")
    lines.append(f"Início em: {start_state}")
    lines.append("")  # linha em branco

    # Ordena estados apenas para saída mais estável/legível
    for name in sorted(states.keys()):
        sdef = states[name]
        transitions = sdef.get("on", [])

        header = f"[{name}]"
        if not transitions:
            header += " (fim)"
        lines.append(header)

        # Texto de resposta do estado (se houver)
        if "respond" in sdef:
            lines.append(f"  responde: \"{sdef['respond']}\"")

        # Transições de saída
        for t in transitions:
            intent = t.get("intent", "<intent?>")
            target = t.get("to", "<estado?>")
            lines.append(f"  |--[{intent}]--> {target}")

        lines.append("")  # linha em branco entre estados

    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python tools/visualize_chatflow.py <arquivo_ir.json>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.is_file():
        print(f"Arquivo não encontrado: {path}")
        sys.exit(1)

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Erro ao ler JSON: {e}")
        sys.exit(1)

    output = build_ascii_flow(data)
    print(output)


if __name__ == "__main__":
    main()
