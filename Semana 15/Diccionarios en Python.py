informacion_personal ={ #Creo el diccionario
"Nombre:" :"Dennis",
"Edad:" : "18",
"Ciudad:" : "Nueva Loja",
"Profesion:" : "Bachiller"}


informacion_personal["Ciudad:"] = "Riobamba" #Aqui modifico la informacion de Cuidad
informacion_personal["Profesion:"] = "Igenierio en Tics" #Aqui tambien se modifica la informacion de profesion

if "Telefono:" not in informacion_personal: #Aqui con el IF verifico si Telefono esta en el diccionario y si no esta que lo agregue
    informacion_personal["Telefono:"] = "0997119351"

informacion_personal.pop("Edad:", None) #Aqui con "pop" Elimino la palabra Edad del diccionario
print(informacion_personal) # imprimo el diccionario

