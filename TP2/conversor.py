import re

def markdown_to_html(markdown_text: str) -> str:
    linhas = markdown_text.splitlines()
    html_linhas = []
    em_lista = False

    for linha in linhas:
        # 1. Lista numerada (linhas começadas por dígitos seguidos de ponto: '1. item')
        match_lista = re.match(r"^\s*\d+\.\s+(.*)$", linha)
        if match_lista:
            if not em_lista:
                html_linhas.append("<ol>")
                em_lista = True
            conteudo_item = match_lista.group(1)
            conteudo_item = processa_inline(conteudo_item)
            html_linhas.append(f"<li>{conteudo_item}</li>")
            continue
        else:
            if em_lista:
                html_linhas.append("</ol>")
                em_lista = False

        # 2. Cabeçalhos (# texto, ## texto, ### texto, etc.)
        match_header = re.match(r"^(#{1,6})\s+(.*)$", linha)
        if match_header:
            nivel = len(match_header.group(1))
            conteudo_header = processa_inline(match_header.group(2))
            html_linhas.append(f"<h{nivel}>{conteudo_header}</h{nivel}>")
            continue

        # Linhas de texto comum
        if linha.strip():
            html_linhas.append(processa_inline(linha))
        else:
            html_linhas.append("")

    if em_lista:
        html_linhas.append("</ol>")

    return "\n".join(html_linhas)


def processa_inline(texto: str) -> str:
    """Processa formatação inline: imagens, links, bold e itálico."""
    # Imagem: ![texto alternativo](caminho) -> deve ser processada antes do link!
    texto = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', texto)

    # Link: [texto](URL)
    texto = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto)

    # Bold: **texto**
    texto = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto)

    # Itálico: *texto* (que não seja parte de **)
    texto = re.sub(r"(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)", r"<i>\1</i>", texto)

    return texto


# Teste com os exemplos fornecidos na aula
if __name__ == "__main__":
    exemplo_md = """# Exemplo

Este é um **exemplo** com texto em *itálico*.

Lista numerada:
1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ..."""

    print("=== ENTRADA MARKDOWN ===")
    print(exemplo_md)
    print("\n=== SAÍDA HTML ===")
    print(markdown_to_html(exemplo_md))
