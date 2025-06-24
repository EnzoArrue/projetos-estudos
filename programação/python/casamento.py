#Mariana e Lucas vão casar e fizeram listas separadas de convidados, podendo haver nomes repetidos dentro da mesma lista ou entre elas. 
#Crie um programa que receba pares de entradas contendo o nome do convidado e quem o convidou (“noivo” ou “noiva”), até a palavra “ACABOU” ser digitada.
#O programa deve gerar e exibir, em ordem alfabética, as seguintes listas, com seus respectivos títulos e formatação:
#Lista final de convidados (todos, sem duplicatas);
#Convidados apenas da noiva;
#Convidados apenas do noivo;
#Convidados convidados por ambos;
#Convidados convidados por apenas um dos dois.
#Cada lista deve ser separada pela linha com vinte hífens, e um asterisco * deve ser impresso entre as listas, exceto após a última.

def convidados():
    L = []
    while True:
        entrada = input()
        if entrada == "ACABOU":
            break
        nome, convidou = entrada.split(";")
        L.append([nome.strip(), convidou.strip()])
    return L  

def validacoes(listacasamento):
    listanoiva = set()
    listanoivo = set()
    for convidado in listacasamento:
        nome, convidou = convidado
        if convidou == "noivo":
            listanoivo.add(nome)
        elif convidou == "noiva":
            listanoiva.add(nome)

    print("-" * 20)
    print("LISTA FINAL")
    print("-" * 20)
    for nome in sorted(listanoivo | listanoiva):
        print(nome)
    print("*")

    print("-" * 20)
    print("APENAS NOIVA")
    print("-" * 20)
    for nome in sorted(listanoiva - listanoivo):
        print(nome)
    print("*")

    print("-" * 20)
    print("APENAS NOIVO")
    print("-" * 20)
    for nome in sorted(listanoivo - listanoiva):
        print(nome)
    print("*")

    print("-" * 20)
    print("POR AMBOS")
    print("-" * 20)
    for nome in sorted(listanoivo & listanoiva):
        print(nome)
    print("*")

    print("-" * 20)
    print("POR APENAS UM DELES")
    print("-" * 20)
    for nome in sorted(listanoivo ^ listanoiva):
        print(nome)

def main():
    lista_convidados = convidados()
    validacoes(lista_convidados)
    
if __name__ == "__main__":
    main()
