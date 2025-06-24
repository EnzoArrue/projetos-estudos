#recursiva, contagem progressiva
def cp(n):
    if n == 0:
        return
    else:
        cp(n-1)
        print(n)

