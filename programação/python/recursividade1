Crie uma função recursiva que determine se um número natural entre 0 e 1000 é par, exibindo a frase correspondente.
#Para treinar suas habilidades sobre a técnica recursiva para resolução de problemas,
#você deverá criar um programa que faça a leitura de um número natural N (0 <= N <= 1000) e exiba uma mensagem indicando se N é par.
#Atenção: A resolução do problema só será considerada para nota se seu programa conter uma função RECURSIVA que receba em seu parâmetro um número natural e retorne verdadeiro,
#se o número for par, ou falso, se o número não for par.
#Dica (1): Pense qual o caso mais fácil de número natural par e qual o caso mais fácil de número natural não par.
#Dica (2): Você certamente conhece a propriedade de que um número natural X par (X>0) ao ser reduzido em duas unidades
#resulta em outro par. O mesmo vale para um número natural não par, isto é,
#se um natural Y ímpar (Y>1) for reduzido em duas unidades, o resultado ainda será um ímpar.
#Um número natural N (0 <= N <= 1000).
#A frase 'numero par' (sem apóstrofos, sem acentuação e com todos os caracteres em minúsculo) caso o número seja par,
#ou 'numero nao par' (sem apóstrofos, sem acentuação e com todos os caracteres em minúsculo) caso o número não seja par.

def coletar_numeros():
    n = int(input())
    while not 0<= n <= 1000:
        n=int(input())
    return n


def paridade(n):
    if n == 0:
        return True
    if n == 1:
        return False
    else:
        return paridade(n-2)

def main():
    n = coletar_numeros()
    if paridade(n)== True:
        print("numero par")
    else:
        print("numero nao par")
            
if __name__ == "__main__":
    main()
    
    
    

