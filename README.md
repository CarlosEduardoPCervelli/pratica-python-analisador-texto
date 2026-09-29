# Analisador de Texto

Script Python que lê um arquivo `.txt` e mostra:
- número de linhas
- total de palavras
- palavra mais frequente (e quantas vezes ela aparece)

## Como funciona

- `re.findall(r"[a-zà-ú]+", texto)` extrai só sequências de letras, ignorando
  pontuação, números e espaços — assim "gato." e "gato" contam como a mesma
  palavra.
- `collections.Counter` conta a frequência de cada palavra e `most_common(1)`
  retorna a mais frequente.
- Tudo é convertido para minúsculas antes de contar, para "Gato" e "gato"
  não serem tratados como palavras diferentes.

## Como executar

```bash
python3 analisador.py exemplo.txt
```

Saída esperada com o `exemplo.txt` incluído:

```
Número de linhas: 3
Total de palavras: 17
Palavra mais frequente: 'o' (4 ocorrências)
```

## Possíveis melhorias futuras
- Ignorar "stopwords" (artigos, preposições) para achar a palavra de conteúdo
  mais frequente.
- Gerar um pequeno relatório com as top 5 palavras mais usadas.
