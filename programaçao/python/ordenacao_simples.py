#Crie um programa em Python que ordene uma lista de números inteiros usando o algoritmo Bubble Sort, dividido em funções auxiliares. 
#O programa deve gerar uma lista com valores aleatórios, verificar se está ordenada, trocar elementos fora de ordem e usar a função empurra 
#para posicionar o maior elemento no final da lista. Por fim, mostre a lista original e a lista ordenada.from random import randint
# Gera lista com valores aleatórios entre 10 e 99
def gera(n):
    L1 = []
    for i in range(n):
        L1.append(randint(10, 99))
    return L1

# Gera lista com valores aleatórios dentro de um intervalo personalizado
def gera1(n, vmin, vmax):
    L2 = []
    for i in range(n):
        L2.append(randint(vmin, vmax))
    return L2

# Verifica se a lista está em ordem crescente
def crescente(L, n):
    i = 0
    while i < n - 1:
        if L[i] > L[i + 1]:
            return False
        i += 1
    return True

# Troca dois elementos da lista
def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

# Empurra o maior valor para o final da lista até a posição n
def empurra(L, n):
    i = 0
    while i < n - 1:
        if L[i] > L[i + 1]:
            troca(L, i, i + 1)
        i += 1
    return L

# Bubble sort completo
def bubble_sort(L):
    n = len(L)
    for i in range(n - 1, 0, -1):
        empurra(L, i + 1)
    return L

# Teste:
lista = gera(10)
print("Lista original:", lista)
ordenada = bubble_sort(lista.copy())
print("Lista ordenada:", ordenada)

