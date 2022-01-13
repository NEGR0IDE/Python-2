# Actividad Python - Listas
#    ♦ Franco Vedia
#    ♦ Ejercicio 3

#Codificar en Python un programa que permita cargar una lista que contenga.
#las notas de un curso de 20 alumnos (controlar que las notas válidas son entre 0 y 10).

# A)
for i in range (20):
    Notas_Cargadas=input("Ingrese las notas: ")
    Solo_Numeros= Notas_Cargadas.isnumeric()
Notas= Notas_Cargadas.split(",")
if Solo_Numeros == "True" :
    print (f"Las Notas Cargadas son:  {Notas}")
if Solo_Numeros == "False":
    print ("Caracter no valido...")




