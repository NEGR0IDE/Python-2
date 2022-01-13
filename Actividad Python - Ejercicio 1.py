# Actividad Python - Listas
#    ♦ Franco Vedia
#    ♦ Ejercicio 1

# Codificar en Python un programa que cargue una lista A con 10 
# elementos numéricos y realice las siguientes modificaciones:

# a) Asignar el valor 11,2 a la tercer posición de la lista A

A= [1,2,3,4,5,6,7,8,9,10]
A[3]= 11,2

# b) Asignar el valor del elemento de la octava posición de la lista A en la segunda posición

A[1]=A[7]

# c) Intercambiar el elemento de la cuarta posición, con el de la novena posición de la lista A

Aux=0
Aux=A[4]
A[3]=A[8]
A[8]=Aux

print(A)