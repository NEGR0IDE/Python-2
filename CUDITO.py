import os

def ingresar_nombre():
    """ funcion para ingresar un nombre """
    while True:
        nombre = input("Ingrese el nombre del estudiante : ")
        if nombre=="":
            pass
        else:
            return nombre

def ingresar_nota():
    """ funcion para ingresar una nota """
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0-10):"))
            if 0<=nota<=10:
                return nota
            else:
                print("la nota tiene que estar entre 0 y 10")
        except:
            print("la nota tiene que ser un valor numerico")
 
 def continuar():
    """ funcion para ingresar un nombre """
    while True:
        nombre = input("Ingrese el nombre del estudiante : ")
        if nombre=="":
            print("el nombre no puede estar vacio")
        else:
            return nombre

def promedio_notas(lista_notas):
    """ funcion para mostrar el  promedio de notas de los estudiantes """
    if len(estudiantes)==0:
        return -1
    return sum(lista_notas)/len(lista_notas)
 
def Menu():
    print("""-------------------------------------------------------
    Selecciona una opción...
    1 - Agregar estudiante
    2 - Buscar estudiante por nombre
    3 - Modificar nota
    4 - Listado ordenados por nombres
    5 - Listado ordenados por notas
    6 - Mostrar promedio de las notas
    7 - Borrar un estudiante
    8 - Calcular la edad promedio de los estudiantes
    0 - Salir""")

# --------------- Programa principal----------------------------

# definimos la lista que contendra una lista con cada estudiante
estudiantes = []
# definimos la lista que contendra las notas de cada estudiante
notas =[]
edades =[]

while True:
    Menu ()
 
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion=-1
 
    if opcion == 1:
        estudiantes.append(ingresar_nombre())
        notas.append(ingresar_nota())
        print(estudiantes)
        print(notas)
        os.system("pause")

    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
        
    elif opcion == 6:

        promedio= promedio_notas(notas)
        print(promedio)
        os.system("pause")
        
    elif opcion == 7:
        pass
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")