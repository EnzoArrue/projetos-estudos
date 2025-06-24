#Crie uma função recursiva que resolva o problema da Torre de Hanoi para n discos, exibindo os movimentos necessários.
def hanoi(n, origem, auxiliar, destino):
    if n == 0: return
    hanoi(n-1,origem, destino, auxiliar)
    print(f"{origem} -> {destino}")
    hanoi(n-1,auxiliar, origem, destino)
    
