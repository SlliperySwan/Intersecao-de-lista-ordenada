def buscaBinaria(L, inicio, fim, numero):
    if inicio > fim:
        return []
    else:
        meio = (inicio + fim)//2
        if  L[meio] > numero:
            return buscaBinaria(L, inicio , meio - 1, numero)
        elif L[meio] < numero:
            return buscaBinaria(L, meio + 1, fim, numero)
        else:
            return [L[meio]]

def intersecao2(A, inicioA, fimA, B):
    if inicioA > fimA:
        return []
    else:
        meio = (inicioA + fimA)//2
        arrayMenor = intersecao2(A, inicioA, meio - 1, B)
        arrayMaior = intersecao2(A, meio + 1, fimA, B)
        termoComum = buscaBinaria(B, 0, len(B) - 1, A[meio])
        return arrayMenor + termoComum + arrayMaior 

def intersecao(A, B):
    tamA = len(A)
    tamB = len(B)
    if tamB >= tamA:
        return intersecao2(A, 0, tamA - 1, B)
    else:
        return intersecao2(B, 0, tamB - 1, A)