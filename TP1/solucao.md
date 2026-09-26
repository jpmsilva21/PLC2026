## TP1

# Expressão regular para apanhar Strings Binárias que não contenham a substring "011"

`^1*(0+1?)*$`

## Explicação:

- Começamos com `^` para garantir que a validação começa no início
- No início, podemos ter nenhum ou vários 1's então começamos com `1*`
- De seguida, agrupamos os blocos em `(0+1?)*`:
  - `0+`: sempre que surge um zero, garantimos que é uma sequência de pelo menos um ou mais zeros
  - `1?`: a seguir a essa sequência de zeros só é permitido surgir no máximo um 1 (ou nenhum) para não termos o 011
  - `*`: este padrão pode repetir-se zero ou muitas vezes ao longo da string
- Assim, é impossível surgir a sequência 011, cobrindo também casos terminados em 0
- Acabamos com `$` para garantir que a validação vai até ao último dígito

## Exemplos de Teste:

- 01111110 -> Rejeitada (contém "011")
- 1100 -> Aceite
- 011011 -> Rejeitada (contém "011")
- 101111 -> Rejeitada (contém "011")
- 1101 -> Aceite
- 1010101010 -> Aceite
- 0000 -> Aceite

---

## Implementação em Python

Para validar a expressão regular de forma automatizada, implementei este script em Python:

```python
import re

def valida_string_binaria(texto: str) -> bool:
    padrao = r"^1*(0+1?)*$"
    return bool(re.fullmatch(padrao, texto))

testes = ["01111110","1100","011011","101111","1101","1010101010","0000"]

print("=== Validação de Strings Binárias (sem '011') ===")
for t in testes:
    valida = valida_string_binaria(t)
    estado = "Aceite" if valida else "Rejeitada"
    print(f"{t:<12} -> {estado}")
