import re
from typing import NamedTuple, Generator

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def lexer(query: str) -> Generator[Token, None, None]:
    token_specification = [
        ('COMMENT',   r'#[^\n]*'),            
        ('STRING',    r'"[^"\\]*(?:\\.[^"\\]*)*"'), 
        ('VARIABLE',  r'\?[a-zA-Z0-9_]+'),      
        ('LANG',      r'@[a-zA-Z]{2}'),         
        ('NUM',       r'\b\d+\b'),             
        ('KEYWORD',   r'\b(?:select|where|LIMIT)\b'), 
        ('TYPE_KW',   r'\ba\b'),              
        ('CONCEPT',   r'[a-zA-Z_][a-zA-Z0-9_]*(?::[a-zA-Z0-9_]+)?'), 
        ('LBRACE',    r'\{'),                 
        ('RBRACE',    r'\}'),                  
        ('DOT',       r'\.'),                   
        ('NEWLINE',   r'\n'),           
        ('SKIP',      r'[ \t\r]+'),
        ('MISMATCH',  r'.'),
    ]

    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, query):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start

        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind in ('SKIP', 'COMMENT'):
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Caráter inesperado {value!r} na linha {line_num}, coluna {column}")
        
        yield Token(kind, value, line_num, column)


if __name__ == '__main__':
    # Exemplo 
    exemplo = """# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo: MusicalArtist.
?s foaf:name "Chuck Berry"@en
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""

    print(f"{'LINHA':<7} {'COL':<5} {'TIPO':<12} {'VALOR'}")
    print("-" * 45)
    for tok in lexer(exemplo):
        print(f"{tok.line:<7} {tok.column:<5} {tok.type:<12} {tok.value}")
