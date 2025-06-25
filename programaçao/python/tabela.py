# Uma empresa quer premiar seus funcionários de acordo
# com a quantidade de anos que estão contratados e por
# terem cumprido suas metas individuais. Para isso, a
# empresa construirá uma tabela com os nomes dos
# funcionários, salários, anos completos na empresa e
# um campo com um indicativo de que o funcionário
# cumpriu sua meta.
#
# A premiação será um bônus que corresponde ao próprio
# salário do funcionário acrescido de 5% por cada ano
# na empresa. Caso o funcionário tenha cumprido sua
# meta, terá mais 10% sobre o bônus já conquistado.
# 
# 1º) Seu programa deverá ler e armazenar os dados de
#     todos os funcionários;
# 2º) Em seguida, deverá exibir a tabela com os dados
#     dos funcionários. Seja criativo no formato da
#     tabela;
# 3º) Por fim, seu programa exibirá outra tabela com o
#     nome de cada funcionário e seu respectivo bônus.
#
# Obs.(1): O registro de cada funcionário estará em uma
#          única linha, e os campos separados por ';'.
# Obs.(2): A entrada encerrará quando o usuário
#          pressionar [ENTER] sem digitar valores
#          na linha, isto é, com uma linha em branco.
#
# Exemplo de    Matheus Oliveira;1000.0;3;sim [ENTER]
# entrada:      Aline dos Santos;4000.0;4;sim [ENTER]
#               Carla Oliveira;2500.0;2;não   [ENTER]
#               Leon Kennedy;10000.0;10;sim   [ENTER]
#               <linha vazia>                 [ENTER]
#
# Como o exemplo de entrada será interpretado:
#
# ------------------------------------------------
#       NOME        |   SALÁRIO   |  TEMPO  | META
# ------------------------------------------------
# Matheus Oliveira  | R$  1000.00 | 03 anos | sim
# Aline dos Santos  | R$  4000.00 | 04 anos | sim
# Carla Oliveira    | R$  2500.00 | 02 anos | não
# Leon Kennedy      | R$ 10000.00 | 10 anos | sim
# ------------------------------------------------
#
# Como o exemplo de entrada será armazenado em Python:
#
# #                       0               1      2    3
# funcionarios = [['Matheus Oliveira',  1000.0,  3, True ], # 0
#                 ['Aline dos Santos',  4000.0,  4, True ], # 1
#                 ['Carla Oliveira',    2500.0,  2, False], # 2
#                 ['Leon Kennedy',     10000.0, 10, True ]] # 3

def exibe_funcionarios(funcionarios):
    print('-' * 50)
    print(f'{"NOME":^16} | {"SALÁRIO":^11} | {"TEMPO":^7} | {"META":^4}')
    print('-' * 50)
    for funcionario in funcionarios:
        nome, salario, tempo, meta = funcionario
        print(f'{nome:16} | ', end='')
        print(f'R$ {salario:8.2f} | ', end='')
        print(f'{tempo:02} anos | ', end='')
        if meta:
            print(f'{"😁":^4}')
        else:
            print(f'{"😔":^4}')
    print('-' * 50)

def exibe_bonus(bonus):
    for registro in bonus:
        print(registro)

# ----------------------
# 1ª parte
# ----------------------

funcionarios = []

registro = input('Registro? ')

while registro != '':
    nome, salario, tempo, meta = registro.split(';')
    salario = float(salario)
    tempo = int(tempo)
    if meta == 'sim':
        meta = True
    else:
        meta = False
    funcionarios.append([nome, salario, tempo, meta])
    registro = input('Registro? ')

# ----------------------
# 2ª parte
# ----------------------

exibe_funcionarios(funcionarios)

# ----------------------
# 3ª parte
# ----------------------

bonus = []

for funcionario in funcionarios:
    nome, salario, tempo, meta = funcionario
    valor = salario + (0.05 * tempo * salario)
    if meta: valor += 0.10 * valor
    bonus.append([nome, valor])

exibe_bonus(bonus)
