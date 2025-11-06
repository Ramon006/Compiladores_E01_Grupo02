# Fluxos de Diálogo — Demonstração (3 completos)

Este documento demonstra **três fluxos** completos a partir das regras em `exemplos/chatflow_rules_example.cf`.

## Fluxo 1 — saudação → ajuda → sair
```
Inicio --[saudacao]--> Saudacao
Saudacao --[ajuda]--> Ajuda
Ajuda --[sair]--> Fim
```

## Fluxo 2 — erro direto para fim
```
Inicio --[erro]--> Fim
```

## Fluxo 3 — saudação → sair
```
Inicio --[saudacao]--> Saudacao
Saudacao --[sair]--> Fim
```
