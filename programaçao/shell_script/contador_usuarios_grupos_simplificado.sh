#!/bin/bash

# Desenvolver um script Bash que conta ocorrências de strings em arquivos de usuários e grupos.
# O programa solicita ao usuário uma string para buscar em /etc/passwd (usuários)
# e outra para /etc/group (grupos).
# Ele então exibe a quantidade de correspondências para cada um e a soma total.
# O script inclui pausas para interação do usuário no início, no final e antes da soma.

echo -ne "\n\tPrograma conta qtd usuário e qtd grupos - <ENTER>\n"
read
echo -ne "\n\tDigite string de login de usuário: "; read USU
echo -ne "\n\tDigite string de grupo: "; read GRU
SOMAUSU=$(grep $USU /etc/passwd | wc -l)
SOMAGRU=$(grep $GRU /etc/group  | wc -l)
echo
echo -ne "\n\tQtd usuário com string $USU é $SOMAUSU "
echo -ne "\n\tQtd grupos com string $GRU é $SOMAGRU "
echo -ne "\n\tSoma usuário+grupos: $((SOMAUSU+SOMAGRU)) - <ENTER>\n"
read
echo -ne "\n\tF I M\n\n"
