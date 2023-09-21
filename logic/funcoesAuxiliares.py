from interface.estilos import LINE_BREAK_ANSWER;

def copy(matriz1):
    resultado = [];

    for i in range(0,3):
        aux = [];
        for j in range(0,3):
            aux.append(matriz1[i][j]);
        resultado.append(aux);

    return resultado;

def line_break(texto):
    palavras = texto.split(" ");
    size_words = 0;
    linha = [];
    resultado = [];

    for p in palavras:
        linha.append(p);
        size_words += len(p);
        if size_words >= LINE_BREAK_ANSWER:
            resultado.append(" ".join(linha));
            size_words = 0;
            linha = [];
    resultado.append(" ".join(linha));

    return "\n".join(resultado);