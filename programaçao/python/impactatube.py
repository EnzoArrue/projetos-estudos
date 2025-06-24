#Crie um programa que calcule a bonificação de canais de vídeo com base no número de inscritos, no valor base de monetização e no status de premium.
#O programa deve receber a quantidade de canais e, 
#para cada canal, os seguintes dados separados por ponto e vírgula (;): nome do canal, número de inscritos, valor de monetização base e se é premium (sim ou nao).
#Em seguida, o programa deve ler dois valores numéricos:
#X: valor extra por mil inscritos para canais premium
#Y: valor extra por mil inscritos para canais não premium#
#A bonificação é calculada somando à monetização base um valor proporcional ao número de inscritos (por mil inscritos), de acordo com o status premium.
#Ao final, o programa deve exibir a lista dos canais com suas respectivas bonificações, formatadas com duas casas decimais.
def calcular_bonificacao(canais, x, y):
    resultados = []
    for canal in canais:
        nome, inscritos, monetizacao, premium = canal
        inscritos = int(inscritos)
        monetizacao = float(monetizacao)

        # Calcular a bonificação
        if premium == 'sim':
            bonus = monetizacao + (inscritos // 1000) * x
        else:
            bonus = monetizacao + (inscritos // 1000) * y
        
        resultados.append((nome, bonus))
    return resultados

def main():
    # Ler a quantidade de canais
    n = int(input().strip())
    canais = []

    # Ler os dados dos canais
    for _ in range(n):
        linha = input().strip()
        nome, inscritos, monetizacao, premium = linha.split(';')
        canais.append((nome, inscritos, monetizacao, premium))

    # Ler os valores X e Y
    x = float(input().strip())
    y = float(input().strip())

    # Calcular as bonificações
    resultados = calcular_bonificacao(canais, x, y)

    # Exibir o cabeçalho
    print("-----")
    print("BÔNUS")
    print("-----")

    # Exibir os resultados formatados
    for nome, bonus in resultados:
        print(f"{nome}: R$ {bonus:.2f}")

# Executar o programa
main()
