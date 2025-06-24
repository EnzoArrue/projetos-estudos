#Crie uma função que receba como parâmetros duas listas ordenadas L e M, junto com seus respectivos tamanhos tam1 e tam2.
#A função deve intercalar os elementos das duas listas em uma terceira lista T, de forma que T também permaneça ordenada.
#A função deve retornar a lista T já ordenada com todos os elementos de L e M.

def intercala(L, M, tam1, tam2):
    T = (tam1 + tam2) * [0]
    i, j, k = 0, 0, 0

    while i < tam1 and j < tam2:
        if L[i] < M[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = M[j]
            j += 1
        k += 1

    while i < tam1:
        T[k] = L[i]  # corrigido aqui
        i += 1
        k += 1

    while j < tam2:
        T[k] = M[j]
        j += 1
        k += 1

    return T
