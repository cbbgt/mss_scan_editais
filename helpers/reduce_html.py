
import re


def reduce_html(html: str):
    # Remover espaços desnecessários
    # html_without_spaces = re.sub(r">\s+<", "><", html).strip()
    # Transformar em uma única linha
    html_in_one_line = re.sub(r"\s+", " ", html)
    return html_in_one_line
