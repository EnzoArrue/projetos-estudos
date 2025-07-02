#!/bin/bash

# Desenvolver um script Bash que permite ao usuário pesquisar por strings específicas
# em arquivos de configuração do sistema: /etc/passwd (para usuários) e /etc/group (para grupos).
# O script deve solicitar uma string de usuário e uma string de grupo.
# Em seguida, ele pesquisará e contará quantas ocorrências de cada string são encontradas.
# Se houver resultados, exibirá a contagem; caso contrário, informará que não há resultados.
# Por fim, o script somará o total de ocorrências de usuários e grupos e exibirá o resultado.

echo -e "\tDigite uma string de usuário que deseja ver: "; read USR
echo -e "\tDigite agora, uma string de grupo que deseja: "; read GRU
if grep "$USR" /etc/passwd; then
        resultado=$(grep "$USR" /etc/passwd | wc -l)
        echo -e "\nPossui: $resultado\n"
else
        echo -e "Sem resultados!\n"
fi
if grep "$GRU" /etc/group; then
        r2=$(grep "$GRU" /etc/group | wc -l)
        echo -e "\nPossui: $r2 "
else
        echo -e "\nSem resultados de grupo!\n"
fi
soma=$((resultado + r2))
echo "O resultado da soma é: $soma "
