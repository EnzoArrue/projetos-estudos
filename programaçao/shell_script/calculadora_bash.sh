#!/bin/bash

# Desenvolver um script Bash que funcione como uma calculadora simples, oferecendo um menu de opções.
# O usuário poderá escolher entre as operações de soma, multiplicação ou cálculo do quadrado de um número.
# O script deve validar a entrada do usuário para garantir que uma opção válida seja escolhida.
# Cada operação será realizada por uma função específica, e o resultado será exibido.
# O script também deve permitir que o usuário saia do programa.

function soma() {
        echo -e "\nDigite o 1° número\n"
        read resposta
        echo -e "\nDigite o 2° número\n"
        read resposta2
        rfinal=$(($resposta + $resposta2))
        echo -e "\nO resultado é: "$rfinal""
}
function mult() {
        echo -e "\nDigite o 1° número\n"
        read resposta
        echo -e "\nDigite o 2° número\n"
        read resposta2
        rfinal=$(($resposta * $resposta2))
        echo -e "\nO resultado é: "$rfinal""
}
function quadrado() {
        echo -e "\nDigite o número:\n"
        read resposta
        rfinal=$(($resposta * $resposta))
        echo -e "\nO resultado é: "$rfinal""
}
echo -e "\tDigite o número de uma opção"
echo -e "\n\t====MENU===="
echo -e "\n\tOpção 1 - Soma"
echo -e "\n\tOpção 2 - Multiplicação"
echo -e "\n\tOpção 3 - Quadrado"
echo -e "\n\tOpção 4 - Sair"
read numero
while [ $numero -ne 1 ] && [ $numero -ne 2 ] && [ $numero -ne 3 ] && [ $numero -ne 4 ]; do
        echo -e "\nComando inválido!"
        echo -e "\nDigite o número de uma opção válida:\n"
        echo -e "\n\t====MENU===="
        echo -e "\n\tOpção 1 - Soma"
        echo -e "\n\tOpção 2 - Multiplicação"
        echo -e "\n\tOpção 3 - Quadrado"
        echo -e "\n\tOpção 4 - Sair"
        read numero
done
if [ $numero  -eq 1 ]; then
        soma
elif [ $numero -eq 2 ]; then
        mult
elif [ $numero -eq 3 ]; then
        quadrado
elif [ $numero -eq 4 ]; then
        exit
fi
