matriz = [
    [4, 5, 6],
    [ 7, 8, 9],
    [10, 11, 12],
]
def buscarvalor(matriz, valor):
    for i, fila in enumerate(matriz):
        if valor in fila:
            j = fila.index(valor)
            return (i, j)
    return None

valorbuscado = 8

posicion = buscarvalor(matriz, valorbuscado)

if posicion is not None:
    print(f"El valor {valorbuscado} se encuentra en la posicin {posicion}")
else:
    print(f"El valor {valorbuscado} no se encontro en la matriz")