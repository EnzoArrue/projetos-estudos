#Crie uma função recursiva que receba um número natural e retorne a quantidade de dígitos que ele possui.
# Crie uma função que receba em seu único parâmetro n um
# número natural e devolva como resposta a quantidade de
# dígitos de n.
# Obs.1: A função deve ser recursiva.
# Obs.2: Não converta o número dado no parâmetro.
# Dica: Comece pensando qual a base da recursão, isto é,
#       qual o caso mais simples para responder quantos
#       dígitos um número natural pode ter.
def qtd_digitos(n):
    if n <= 9:

        return 1

    else:

        resp = qtd_digitos(n//10)

        return resp + 1
