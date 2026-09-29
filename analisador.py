"""
Analisador de texto: lê um arquivo .txt e retorna:
- contagem total de palavras
- palavra mais frequente
- número de linhas
"""

import re
import sys
from collections import Counter


def analisar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    numero_linhas = len(linhas)

    texto_completo = "".join(linhas).lower()
    # extrai só sequências de letras (ignora pontuação e números)
    palavras = re.findall(r"[a-zà-ú]+", texto_completo)

    total_palavras = len(palavras)

    contagem = Counter(palavras)
    palavra_mais_frequente, frequencia = (None, 0)
    if contagem:
        palavra_mais_frequente, frequencia = contagem.most_common(1)[0]

    return {
        "numero_linhas": numero_linhas,
        "total_palavras": total_palavras,
        "palavra_mais_frequente": palavra_mais_frequente,
        "frequencia": frequencia,
    }


def main():
    if len(sys.argv) != 2:
        print("Uso: python analisador.py caminho/para/arquivo.txt")
        sys.exit(1)

    caminho = sys.argv[1]

    try:
        resultado = analisar_arquivo(caminho)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        sys.exit(1)

    print(f"Número de linhas: {resultado['numero_linhas']}")
    print(f"Total de palavras: {resultado['total_palavras']}")
    if resultado["palavra_mais_frequente"]:
        print(
            f"Palavra mais frequente: '{resultado['palavra_mais_frequente']}' "
            f"({resultado['frequencia']} ocorrências)"
        )
    else:
        print("O arquivo não contém palavras.")


if __name__ == "__main__":
    main()
