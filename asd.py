

asd= [1]
abc= ["uno"]
asd1= [50]

def ordenar_x_nombre (nombres,edades,notas):
    UnirListas= tuple(zip(nombres,edades,notas))
    resultado= sorted(UnirListas,reverse=True)
    for dato in resultado:
        print(dato)
        
        
ordenar_x_nombre(abc,asd,asd1)