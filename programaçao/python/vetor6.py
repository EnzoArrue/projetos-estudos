#Crie um programa que solicite ao usuário para inserir 5 números inteiros e armazene-os em uma lista (vetor).
# Em seguida, o programa deve pedir ao usuário para escolher uma posição (índice) de 0 a 4
#e exibir o número correspondente a essa posição na lista.

v = [] 
for i in range(5):
    n=int(input(f"Digite o {i+1}° número da lista: "))
    v.append(n)

posiçao = int(input("Digite uma posição de 0 a 4: "))
while posiçao not in [0,1,2,3,4]:
    posiçao = int(input("Digite uma posição válida de 0 a 4: "))

print(f"O elemento da posição selecionada é: {v[posiçao]}")


#PROGRAMA SE O USUÁRIO QUISESSE ESCOLHER NÚMEROS ALEATÓRIOS.

v = []
qtd_numeros = int(input(f"Digite quantos números deseja adicionar na lista: "))
for i in range(qtd_numeros):
    n=int(input(f"Digite o {i+1}° número da lista: "))
    v.append(n)

posiçao = int(input(f"Digite uma posição de 0 a {qtd_numeros - 1}: "))
while posiçao not in range(0, qtd_numeros):
    posiçao = int(input(f"Digite uma posição válida de 0 a {qtd_numeros - 1}: "))

print(f"O elemento da posição selecionada é: {v[posiçao]}")

