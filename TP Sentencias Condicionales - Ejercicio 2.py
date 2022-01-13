print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Ejercicio 2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print()
print("A continuación ingrese dirección que figura en DNI...")
print()
Calle=input("Ingrese el nombre de la calle : ")
Numero_Casa=int(input("Ingrese el numero de la casa : "))
Localidad=input("Ingrese la localidad donde vive :")
Residente=(Calle,"numero",Numero_Casa,Localidad)

#######################################################################################################
Edad=int(input("Ingrese edad : "))
Multas=int(input("Ingrese cantidad de multas: "))
Edad_Minima= 17
if Localidad=="Maipu" or "Maipú" and Edad>Edad_Minima and Multas==0:
    print("Renovacion habilitada.")
else:
    print("Renovacion no realizada.")