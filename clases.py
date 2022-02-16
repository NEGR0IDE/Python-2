class Celulares: #Definir como clase con la palabra "class" y terminar con ":" dos puntos.
    def __init__ (self, marca, modelo,año): #Metodo constructor 
        self.marca= marca                            #*Self.nombre del atributo
        self.modelo= modelo                          
        self.año= año                                
    def mostrarDatos(self):                 #Defino una funcion para mostrar los datos de la clase celulares
        return (f"El celular de la marca {self.marca}, modelo {self.modelo} fue lanzado al mercado en el año {self.año}.")

class TecladoDeBotones(Celulares):
    def __init__(self,marca,modelo,año,teclado):
        super().__init__(marca,modelo,año)
        self.teclado= teclado
    def mostrar_datos_botones(self):
        return (f"El celular {self.marca} {self.modelo} posee un teclado {self.teclado}.")

class TecladoTactil(Celulares):
    def __init__(self,marca,modelo,año,teclado,android):
        super().__init__(marca,modelo,año)
        self.teclado= teclado
        self.android= android
    def mostrar_datos_tactil(self):
        return (f"El celular {self.marca} {self.modelo} posee un teclado {self.teclado} y tiene android {self.android}.")



Marca= "Nokia"
Modelo= "1100"
Año= "2003"
Teclado= "fisico"

Marca2="LG"
Modelo2="K9"
Año2= "2017"
Teclado2= "tactil"
Android2= "7.1.2"

Nokia=TecladoDeBotones(Marca,Modelo,Año,Teclado)
Lg= TecladoTactil(Marca2,Modelo2,Año2,Teclado2,Android2)

print(Nokia.mostrarDatos())
print(Nokia.mostrar_datos_botones())

print(Lg.mostrarDatos())
print(Lg.mostrar_datos_tactil())
