def ordenar_x_nota (notas,nombres,edades):
    #Funcion para ordenar por nota...
    try:
        nuevaTupla= zip(nombres,edades,notas)
        Tupla_por_notas= sorted(nuevaTupla)
        DatosAlumnos= []
        for Indice in Tupla_por_notas:
            DatosAlumnos.append(Indice)
        return Tupla_por_notas
    except:
        print("La lista posee un solo estudiante.")


nombres=["a","b","c"]
notas=[1,2,3]
edades=[22,33,45]

print(ordenar_x_nota(nombres,notas,edades))