# Actividad Python - Listas
#    ♦ Franco Vedia
#    ♦ Ejercicio 2

#Cargar dos listas: uno con el número de empleado y otro con las horas trabajadas por cada empleado.
#Cada lista tendrá 10 elementos. Se pide:

# A) Promedio de horas trabajadas.

numero_de_empleado= [1,2,3,4,5,6,7,8,9,10]
horas= [10,20,30,40,50,60,70,80,90,100] 
promedio= int(sum(horas)) / int(len(numero_de_empleado))
print (f"El promedio de horas trabajadas es: {promedio}")


# B)
TrabajaronMas=[]
for i in range (len(horas)):
    if horas[i] > promedio:
        TrabajaronMas.append(i)
print (f"Los empleados que mas horas trabajaron son: {TrabajaronMas}")

# C)
Mayor= max(horas)
for o in range (len(horas)):
    if horas[o] >= Mayor:
        print (f"El empleado que mas trabajo fue el: {numero_de_empleado[o]}")

Menor= min(horas)
for e in range (len(horas)):
    if horas[e] <= Menor:
            print (f"El empleado que menos trabajó fue {numero_de_empleado[e]}")
