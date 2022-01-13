# Ejercicio1

Cadena="12,13,122,S,SA,$,%"
Lista= Cadena.split(",")
Lista.pop(3)
Lista.pop(3)
Lista.pop(3)
Lista.pop(3)
print (Lista)

#Ejercicio2


Entrada=0
Entrada=input("Ingresar Cuit: ")
def validarCuit (Hasta_13_Carcteres):
    Cadena1= Entrada.split(",")
    Cantidad_de_Caracteres=len(Cadena1)
    if Cantidad_de_Caracteres == 13 and Solo_Numeros >= 0 and Solo_Numeros[2] == "-":
        Respuesta= "True"
    elif Cantidad_de_Caracteres != 13:
        Respuesta="False"
    return (Respuesta)

def validar_Cuit (Solo_Numeros123):
    Solo_Numeros= "Entrada".isnumeric()
    Lista=Entrada.slpit(",")
    if Solo_Numeros == True:
        Respuesta2= "True"
    elif Solo_Numeros== False:
        Respuesta2= ("False")


print (validar_Cuit(Entrada))

print (validarCuit(Entrada))
    

