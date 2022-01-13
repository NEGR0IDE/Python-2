print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Ejercicio 3 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print()
a= int(input("Ingrese el valor de a: "))
b= int(input("Ingrese el valor de b: "))
x=0
if a == 0 and b == 0:
    print("X tiene infinitas soluciones")
elif a == 0 and b !=0:
    print("No tiene solución")
elif a != 0:
    x = -b/a
    print("La ecuación tiene una única solución, es: ",(x))