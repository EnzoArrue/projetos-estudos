#!/bin/bash
echo "Digite o primeiro número:"
read nmr1
echo "Digite o segundo número:"
read nmr2
if [ $nmr1 -lt $nmr2 ]; then
        echo "$nmr1 é menor que $nmr2"
elif [ $nmr1 -gt $nmr2 ]; then
        echo "$nmr1 é maior que $nmr2"
elif [ $nmr1 -eq $nmr2 ]; then
        echo "$nmr1 é igual que $nmr2"
fi
