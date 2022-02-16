class Celulares: #Definir como clase con la palabra "class" y terminar con ":" dos puntos.
    def ___init__ (self, marca, modelo,android): #Metodo constructor 
    self.marca= marca                            #Self.nombre del atributo
    self.modelo= modelo
    self.android= android

    def antiguo_o_moderno(self):
        if self.android> 9:
            print(f"self.marca,self.modelo,es un celular moderno")
        else:
            print (self.marca,self.modelo,"es un celular antiguo")

Nokia= Celulares("LG","K9",10)





class alumno:  #Definir clase con palabra reservada "class" y cerrar con dos puntos " : " .
    def __init__(self,edad,nombre,nota) #Definir método constructor y argumentos de la clase. Servirán para introducir la información de la clase/objeto. 
        self.edad = int(edad)                                            #Utilizar "self.nombreAtributo = argumentoAtributo" para guardar la información que se le pasa al objeto mediante argumentos.
        self.nombre = nombre
        self.nota = float(nota)
    def mostrarDatos(self):
        return (f"{self.nombre} tiene {self.edad} años y su nota es {self.nota}.")


alumno1=alumno(22,"Tomas Ponce",10)


print(usuario1.mostrarDatos())

