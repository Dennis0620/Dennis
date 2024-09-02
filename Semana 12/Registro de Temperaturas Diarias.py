Ciudades = ["Lago Agrio" , "Quito"]
Dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
semanas = 2
matrix_temperaturas= [
    [#Lago Agrio
        [30, 29, 33, 28, 26, 31, 30],
        [34, 31, 28, 27, 29, 30, 35],
    ],
    [#Quito
        [17, 22, 23, 20, 21, 17, 16],
        [23, 20, 18, 16, 19, 20, 22]
    ]
]


for idx_ciudad, ciudad in enumerate(Ciudades):
    print(f"Promedios de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma = 0
        for dia in range(len(Dias)):
            suma += matrix_temperaturas[idx_ciudad][semana][dia]
        promedio = suma / len(Dias)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()