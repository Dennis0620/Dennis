matriz = [
    [9,13,18],
    [3,7,4],
    [8,3,16]
]

def bubble_sort_fila(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)

    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    matriz[fila_index] = fila

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 1
bubble_sort_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
