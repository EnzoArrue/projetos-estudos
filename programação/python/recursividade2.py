# Recursividade, contagem regressiva.
def cr(n):
    if n == 0:
        return
    else:
        print(n, end=' ')
        cr(n-1)

