#Solicite um número natural N e informe se ele é primo ou não.
def primo(n):
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1

    if qtd == 2:              #2 divisores (primo)
        return True
    else:
        return False

n= int(input("Digite um valor: "))
if primo(n):
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo!")
