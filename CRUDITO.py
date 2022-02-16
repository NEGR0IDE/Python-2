import os
import math

def ingresar_nombre():
    #Funcion para ingresar un nombre...
    while True:
        nombre = input("Ingrese el nombre del estudiante : ")
        if nombre=="":
            print("El nombre no puede estar vacio")
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
                print("La nota tiene que estar entre 0 y 10")
        except:
            print("La nota tiene que ser un valor numerico")
 
def ingresar_edad():
    #Funcion para ingresar la edad...
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad == "":
                print("La edad no puede estár vacia")
            else:
                return edad
        except:
            print("La edad tiene que ser un valor numerico")

def imprimir_listas(nombres,edades,notas):
    #Funcion para unir las listas en una tupla...
    UnirListas= zip(nombres,edades,notas)
    for Lista in UnirListas:
        print (Lista)
            
def promedio_notas(ListaNotas):
    # Funcion para mostrar el  promedio de notas de los estudiantes...
    if len(ListaNotas)==0:
        return -1
    else:
        return sum(ListaNotas)/len(ListaNotas)

def buscar_estudiante(ListaNombre,ListaNota,ListaEdad):
    #Funcion para buscar por nombre...
    alumno=input("Ingrese el nombre del estudiante que desea buscar: ")
    resultado= ListaNombre.index(alumno)
    print(f""" El alumno {alumno} tiene {ListaEdad[resultado]} años de edad y su nota es {ListaNota[resultado]}""")

def modificar_nota(ListaNombre,ListaNota):
    #Funcion para modificar notas...
    NombreDelAlumno= input("Ingrese el nombre del alumno que desea cambiarle la nota: ")
    NotaNueva= float(input("Ingrese la nota nueva: "))
    Indice_A_Cambiar= ListaNombre.index(NombreDelAlumno)
    ListaNota[Indice_A_Cambiar]= NotaNueva
    datoAimprimir=zip(ListaNombre,ListaNota)
    datosAlumnos=[]
    for i in datoAimprimir:
        datosAlumnos.append(i)
    return datosAlumnos

def ordenar_x_nombre (nombres,notas,edades):
    #Funcion para ordenar por nombre...
    if len (nombres) < 2:
        return "La lista alumnos está incompleta."
    else:
        nuevaTupla= zip(nombres,edades,notas)
        Tupla_por_nombres= sorted(nuevaTupla)
        datosOrdenados= []
        for Indice in Tupla_por_nombres:
            datosOrdenados.append(Indice)
        return datosOrdenados

def ordenar_x_nota (notas,nombres,edades):
    #Funcion para ordenar por nota...
    try:
        nuevaTupla= zip(nombres,edades,notas)
        Tupla_por_notas= sorted(nuevaTupla)
        DatosAlumnos= []
        for Indice in Tupla_por_notas:
            DatosAlumnos.append(Indice)
        return DatosAlumnos
    except:
        print("La lista posee un solo estudiante.")

def borrar_alumno (ListaNombres,ListaEdades,ListaNotas):
    #Funcion para borrar un alumno...
    try:
        alumno_A_borrar=input("Ingrese el nombre del alumno que desea borrar: ")
        indice_alumno= alumno_A_borrar.index(alumno_A_borrar)
        ListaNombres.pop(indice_alumno)
        ListaEdades.pop(indice_alumno)
        ListaNotas.pop(indice_alumno)
        Lista_Mod= zip(ListaNombres,ListaEdades,ListaNotas)
        for Lista in Lista_Mod:
            print (Lista)
    except:
        print("Debe cargar al menos un estudiante...")

def edad_promedio (ListaEdades):
    #Funcion para mostrar el promedio de edad...
        if len(ListaEdades)==0:
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
        while True:
            AgregarNombres=estudiantes.append(ingresar_nombre())
            AgregarEdades=edades.append(ingresar_edad())
            AgregarNotas=notas.append(ingresar_nota())
            os.system("cls")
            print("El alumno ha quedado guardado con este nombre, esta edad y esta nota:")
            imprimir_listas(estudiantes,edades,notas)
            print("Si desea agregar otro alumno ingrese enter. Si no desea agregar mas alumnos ingrese cualquier tecla seguida de enter.")
            respuesta=input("")
            if respuesta != "":
                break
        os.system("pause")
    elif opcion == 2:
        buscar_estudiante(estudiantes,notas,edades)
        os.system("pause")
    elif opcion == 3:
        notasNuevas=modificar_nota(estudiantes,notas)
        print("Las nuevas notas son: ")
        print(notasNuevas)
        os.system("pause")
    elif opcion == 4:
        print("Lista ordenada por nombre: ")
        print(ordenar_x_nombre(estudiantes,notas,edades))
        os.system("pause")
    elif opcion == 5:
        print ("Lista ordenadad por notas: ")
        ordenar_x_nota(notas,estudiantes,edades)
        os.system("pause")
    elif opcion == 6:
        print("El promedio de las notas es: ")
        print(promedio_notas(notas))
        os.system("pause")
    elif opcion == 7:
        borrar_alumno(estudiantes,edades,notas)
        os.system("pause")
    elif opcion == 8:
        "La edad promedio es: "
        print(edad_promedio(edades))
        os.system("pause")
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta.")


