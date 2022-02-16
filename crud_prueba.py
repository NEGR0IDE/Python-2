def ingresar_nombre(ListaNombres,ListaNotas,ListaEdades):
    #Funcion para ingresar un nombre...
    while True:
        nombre = input("Ingrese el nombre del estudiante : ")
        edades= input("Ingrese la edad del alumno: ")
        if nombre=="":
            print("El nombre no puede estar vacio.")
        except:
            print("La nota tiene que ser un valor numerico")
            ListaNombres.append(nombre)
            ListaNotas.append(nota)
            ListaEdades.append(edades)
            tupla= zip(ListaNombres,ListaNotas,ListaEdades)
            for i in tupla:
                return i
        try:
            if 0<=nota<=10:
                return nota
            else:
                print("La nota tiene que estar entre 0 y 10")
        except:
            print("La nota tiene que ser un valor numerico")

estudiantes=[]
notas=[]
edades=[]
TuplaDatos=ingresar_nombre(estudiantes,notas,edades)
print(TuplaDatos)









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
            edad = input("Ingrese la edad del estudiante: ")
            if edad == "":
                print("La edad no puede estár vacia")
            else:
                return edad
        except:
            print("La edad tiene que ser un valor numerico")

