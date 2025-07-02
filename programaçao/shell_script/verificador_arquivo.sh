#!/bin/bash

# Desenvolver um script Bash que verifique a existência de um arquivo especificado em um determinado caminho.
# Se o arquivo for encontrado, o programa deverá informar ao usuário que o arquivo existe e, em seguida,
# exibir todo o seu conteúdo. Caso contrário, o programa deverá notificar que o arquivo é inválido ou inexistente.

ARQUIVO=/home/kali/scripts_shell/teste_simbolos/arq1.txt

if [ -f "$ARQUIVO" ]; then
        echo "Arquivo Existe!"
        cat "$ARQUIVO"
else
        echo "Arquivo inválido ou inexistente!"
fi
