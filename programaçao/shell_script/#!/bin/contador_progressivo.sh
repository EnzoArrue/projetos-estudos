#!/bin/bash

# Desenvolver um script Bash que exiba uma contagem progressiva de 1 a 5.
# Cada número deve ser mostrado com um intervalo de 2 segundos.
# Ao final da contagem, o script deve exibir a palavra "FIM" de forma estilizada.

cont=0
echo -e "Contagem Progressiva:\n"
while [ $cont -lt 5 ]; do
        cont=$((cont + 1))
        echo -ne "$cont\n"
        sleep 2
done
echo -ne "\n\tFIM"
