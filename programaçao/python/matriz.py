# Enunciado:
# Dada uma matriz 4x3 com valores float, faça o seguinte:
# - Imprima o elemento da quarta linha, primeira coluna.
# - Dobre o valor do elemento da primeira linha, terceira coluna.
# - Calcule e imprima a soma dos elementos da primeira linha.
# - Calcule e imprima a soma dos elementos da primeira coluna.

M = [
    [5.5, 7.0, 8.7],
    [8.0, 6.0, 9.2],
    [7.8, 8.3, 8.5],
    [0.0, 9.9, 9.1]
]

print(M[3][0])  # elemento da quarta linha, primeira coluna

M[0][2] *= 2   # dobra o valor da primeira linha, terceira coluna

soma_linha = 0
for coluna in range(len(M[0])):
    soma_linha += M[0][coluna]

print(f"Soma da primeira linha = {soma_linha:.1f}")

soma_coluna = 0
for linha in range(len(M)):
    soma_coluna += M[linha][0]

print(f"Soma da primeira coluna = {soma_coluna:.1f}")
