class Auto:
    cantidadCreados=0


    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo  
        self.precio = precio  
        self.asientos = asientos 
        self.marca = marca  
        self.motor = motor 
        self.registro = registro  
        cantidadCreados+=1

    def cantidadAsientos(self):
        con=0
        for i in self.asientos:
            if isinstance(i,self.asientos):
                con+=1
        return con
    
    def verificarIntegridad(self):
        for i in self.asientos:
            if i.registro == self.motor.registro and self.motor.registro==self.registro:
                return "Auto original"
            else:
                return "Las piezas no son originales"
            
class Motor:
    
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        lista=["gasolina","electrico"]
        if tipo in lista:
            self.tipo=tipo

    
class Asiento:

    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        lista=["amarillo","negro","blanco","rojo","verde"]
        if color in lista:
            self.color=color
        




        

