TPC1

# Expressão regular para apanhar Strings Binárias que não contenham a substring "011"

`^1*(0+1?)*$`

## Explicação:

- Começamos com `^` para garantir que a validação começa no início
- No início, podemos ter nenhum ou vários 1's então começamos com `1*`
- De seguida, agrupamos os blocos em `(0+1?)*`:
  - `0+`: sempre que surge um zero, garantimos que é uma sequência de pelo menos um ou mais zeros
  - `1?`: a seguir a essa sequência de zeros só é permitido surgir no máximo um 1 (ou nenhum) para não termos o 011
  - `*`: este padrão pode repetir-se muitas vezes ao longo da string
- Assim, é impossível surgir a sequência 011, cobrindo também casos terminados em 0
- Acabamos com `$` para garantir que a validação vai até ao último dígito

## Exemplos de Teste:

- 01111110 -> Rejeitada
- 1100 -> Aceite
- 011011 -> Rejeitada
- 101111 -> Rejeitada 
- 1101 -> Aceite
- 1010101010 -> Aceite
- 0000 -> Aceite
