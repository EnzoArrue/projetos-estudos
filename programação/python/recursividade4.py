#Crie uma função recursiva que converta um número decimal inteiro em sua representação binária e exiba o resultado.
nmr = int(input())

def binario(n):
    if n > 1:  # Corrigido para considerar números maiores que 1
        binario(n // 2)  # Chamada recursiva
    print(f"{n % 2}", end='')  # Impressão em uma única linha

def main():
    binario(nmr)  # Passa o número lido para a função binario

main()



