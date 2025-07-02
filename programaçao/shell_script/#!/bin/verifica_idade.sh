#!/bin/bash

# Desenvolver um script Bash que solicite o nome e a idade do usuário.
# Com base na idade fornecida, o script deve verificar se o usuário é maior de 18 anos.
# Se for maior de idade, o script exibirá uma mensagem de permissão de entrada.
# Caso contrário, exibirá uma mensagem de restrição, indicando que não pode entrar,
# e uma mensagem de "FIM" estilizada.

echo "Qual seu nome?"
read NOME
echo "Qual sua idade?"
read IDADE
if [ $IDADE -ge 18 ]; then
        echo ""$NOME" possui $IDADE, pode entrar!"
else
        echo "Infelizmente "$NOME" possui $IDADE e não poderá entrar!"
        echo -ne "\n\tF\tI\tM"
fi
