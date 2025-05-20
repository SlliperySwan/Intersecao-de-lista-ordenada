def busca_bin(L, inicio, fim, numero):
    if inicio > fim:
        return []
    else:
        meio = (inicio+fim)//2
        if  L[meio] > numero:
            return busca_bin(L, inicio , meio-1, numero)
        elif L[meio] < numero:
            return busca_bin(L, meio+1, fim, numero)
        else:
            return [L[meio]]

def intersecao2(A, inicioA, fimA, B, inicioB, fimB):
    if inicioA > fimA or inicioB > fimB:
        return []
    else:
        meio = (inicioA+fimA)//2
        arrayMenor = intersecao2(A, inicioA, meio - 1, B, inicioB, fimB)
        arrayMaior = intersecao2(A, meio+1, fimA, B, inicioB, fimB)
        termoComum = busca_bin(B, 0, len(B)-1, A[meio])
        existeNoMenor = len(arrayMenor) != 0 and termoComum[0] <= arrayMenor[-1]
        existeNoMaior = len(arrayMaior) != 0 and termoComum[0] >= arrayMaior[0]
        if existeNoMenor or existeNoMaior:
            termoComum = []
        return arrayMenor + termoComum + arrayMaior

def intersecao(A, B):
    return intersecao2(A, 0, len(A)- 1, B, 0, len(B)-1)