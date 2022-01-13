import os

def ingresar_nombre():
    #Funcion para ingresar un nombre...
    while True:
        nombre = input("Ingrese el nombre del estudiante : ")
        if nombre=="":
            print("el nombre no puede estar vacio")
        else:
            return nombre

def ingresar_nota():
    #Funcion para ingresar una nota...
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0-10):"))
            if 0<=nota<=10:
                return nota
            else:
                print("la nota tiene que estar entre 0 y 10")
        except:
            print("la nota tiene que ser un valor numerico")
 
def ingresar_edad():
    #Funcion para ingresar la edad...
    while True:
        try:
            edad = input("Ingrese la edad del estudiante: ")
            if edad == "":
                print("La edad no puede estár vacia")
            else:
                return edad
        except:
            print("La edad tiene que ser un valor numerico")

def unir_listas(nombres,edades,notas):
    #Funcion para unir las listas en una tupla...
    UnirListas= zip(nombres,edades,notas)
    for Lista in UnirListas:
        print (Lista)
    

def promedio_notas(lista_notas):
    # Funcion para mostrar el  promedio de notas de los estudiantes...
    if len(lista_notas)==0:
        return -1
    return sum(lista_notas)/len(lista_notas)

def buscar_estudiante(ListaNombre,ListaNota,ListaEdad):
    #Funcion para buscar por nombre...
    alumno=input("Ingrese el nombre del estudiante que desea buscar: ")
    resultado= ListaNombre.index(alumno)
    print(f""" El alumno {alumno} tiene {ListaEdad[resultado]} de edad y su nota es {ListaNota[resultado]}""")

def modificar_nota(ListaNombre,ListaNota):
    #Funcion para modificar notas...
    NombreDelAlumno= input("Ingrese el nombre del alumno que desea cambiarle la nota: ")
    NotaNueva= input("Ingrese la nota nueva: ")
    Indice_A_Cambiar= ListaNombre.index(NombreDelAlumno)
    ListaNota[Indice_A_Cambiar]= NotaNueva
    print("La lista con la nota cambiada quedá así:")
    print(ListaNota)

def ordenar_x_nombre (nombres,notas,edades):
    #Funcion para ordenar por nombre...
    if len (nombres) < 2:
        return "La lista alumnos está incompleta."
    else:
        nuevaTupla= zip(nombres,edades,notas)
        lista_Ordenada= sorted(nuevaTupla)
        for Indice in lista_Ordenada:
            return Indice
        
def ordenar_x_nota (notas,nombres,edades):
    #Funcion para ordenar por nota...
    UnirListas= zip(notas,nombres,edades)
    for Lista in UnirListas:
        print (Lista)

def borrar_alumno (ListaNombres,ListaEdades,ListaNotas):
    #Funcion para borrar un alumno...
    UnirListas= zip(ListaNombres,ListaEdades,ListaNotas)
    alumno_A_borrar=input("Ingrese el nombre del alumno que desea borrar: ")
    indice_alumno= alumno_A_borrar.index(alumno_A_borrar)
    UnirListas.pop(indice_alumno)
    for Lista in UnirListas:
        print (Lista)

def edad_promedio (ListaEdades):
    #Funcion para mostrar el promedio de edad...
    if len (ListaEdades)== 0:
        return -1
    return sum(ListaEdades)/len(ListaEdades)

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

# ---------------------------- Programa principal ---------------------------- #

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
        AgregarNombres=estudiantes.append(ingresar_nombre())
        AgregarEdades=edades.append(ingresar_edad())
        AgregarNotas=notas.append(ingresar_nota())
        os.system("cls")
        print("El alumno a quedado guardado con este nombre, esta edad y esta nota:")
        unir_listas(estudiantes,edades,notas)
        os.system("pause")
    elif opcion == 2:
        buscar_estudiante(estudiantes,notas,edades)
        os.system("pause")
    elif opcion == 3:
        modificar_nota(estudiantes,notas)
        os.system("pause")
    elif opcion == 4:
        print(ordenar_x_nombre(estudiantes,notas,edades))
        os.system("pause")
    elif opcion == 5:
        ordenar_x_nota(notas,estudiantes,edades)
        os.system("pause")
    elif opcion == 6:
        print(promedio_notas(notas))
        os.system("pause")
    elif opcion == 7:
        borrar_alumno(estudiantes,edades,notas)
        os.system("pause")
    elif opcion == 8:
        edad_promedio(edades)
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta.")


