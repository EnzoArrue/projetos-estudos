#!/bin/bash

# Desenvolver um script Bash que apresente um menu interativo ao usuário.
# O menu oferecerá opções para exibir a data e hora atuais,
# mostrar o nome do usuário logado, ou sair do programa.
# O script deve continuar exibindo o menu até que o usuário escolha a opção de sair.
# Cada funcionalidade (exibir data e nome de usuário) será implementada como uma função separada.

function data() {
        echo  "A data de hoje é: "$(date)""
}
function nomeuser() {
        echo -e "\nO nome do usuário atual é:"$(whoami)""
}
resposta=0
while [ $resposta -ne 3 ]; do
        echo -e "\t====MENU===="
        echo -e "\n\tOpção 1: Data"
        echo -e   "\tOpção 2: Quem sou eu?"
        echo -e   "\tOpção 3: Sair"
        read resposta
        if [ $resposta -eq 1 ]; then
                data
        elif [ $resposta -eq 2 ]; then
                nomeuser
        else
                exit
        fi
done
