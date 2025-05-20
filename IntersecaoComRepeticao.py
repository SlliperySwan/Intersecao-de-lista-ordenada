def busca_bin(Lista, i, f, num):
    if i > f:
        return -1
    else:
        m = int((i+f)/2)
        if  Lista[m] > num:
            return busca_bin(Lista, i , m-1, num)
        elif Lista[m] < num:
            return busca_bin(Lista, m+1, f, num)
        else:
            return m

def intersecao2(A, inicioA, fimA, B, inicioB, fimB):
    if inicioA > fimA or inicioB > fimB:
        return []
    else:
        m = int((inicioA+fimA)/2)
        v1 = intersecao2(A, inicioA, m - 1, B, inicioB, fimB)
        v2 = intersecao2(A, m+1, fimA, B, inicioB, fimB)
        index = busca_bin(B, 0, len(B)-1, A[m])
        inter= []
        if index != -1:
            inter.append(A[m])

        return v1 + inter + v2 

def intersecao(A, B):
    return intersecao2(A, 0, len(A)- 1, B, 0, len(B)-1)
