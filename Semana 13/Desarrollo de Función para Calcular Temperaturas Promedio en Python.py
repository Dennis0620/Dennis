def calculartemperatura(ciudades):
    promediar = {}

    for i, temperatura in enumerate(ciudades):
        promedio = sum(temperatura)/len(temperatura)

        promediar[f"Ciudad Ecuatoriana {i+1}"] = round(promedio, 2)

    return promediar

ciudades = [
    [20,25,22], #Ciudad Ecuatoriana 1
    [29,30,25], #Ciudad Ecuatoriana 2
    [22,19,16]  #Ciudad Ecuatoriana 3
]

promediosc = calculartemperatura(ciudades)

print("El promedio de temperatura de las ciudades son: ")
print(promediosc)