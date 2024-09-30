archivotxt = open('my_notes.txt', "r")
# Colocamos una variable y ponemos el comando open y ponemos el nombre de nuestro archivo de texto, colocamos "R" que es para decir que es solo de lectura

linea1 = archivotxt.readline()
linea2 = archivotxt.readline()
linea3 = archivotxt.readline() #Aqui creamos la cantidad de variables dependiendo la cantidad de lineas tengas en tu archivo de texto

print("\n Contenido del archivo de texto por linea: ")
print("Linea 1:", linea1.strip())
print("Linea 2:", linea2.strip())
print("Linea 3:", linea3.strip()) #Aqui imprimimos por cada linea de texto de nuestro archivo
