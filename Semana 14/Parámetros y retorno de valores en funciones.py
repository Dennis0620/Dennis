def calcular_descuento(montontotal,porcentaje_descuento=25): #Declaracion de la funcion
    descuento = montontotal * porcentaje_descuento / 100
    return descuento

#Programa
monton = 597 #Variable que contiene el primer monton
monton2 = 734 #Variable que contiene el segundo monton
descuento_personalizado = 5

#Primera llamada a la funcion
descuento1 = calcular_descuento(monton)
print(f"El monton del descuento al 10% para el monton {monton} es {descuento1}")

#Segunda llamada a la funcion
descuento2 = calcular_descuento(monton2, descuento_personalizado)
print(f"El monton del descuento ({descuento_personalizado}%) para la compra de {monton2} es {descuento2}")