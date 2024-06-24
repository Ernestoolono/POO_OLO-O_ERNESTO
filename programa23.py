class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.en_marcha = False
    
    def arrancar(self):
        self.en_marcha = True
        print("El coche", self.marca, self.modelo, "ha arrancado.")
    
    def detener(self):
        self.en_marcha = False
        print("El coche", self.marca, self.modelo, "se ha detenido.")
    
    def mostrar_info(self):
        print("Marca:", self.marca, "Modelo:", self.modelo, "Año:", self.año, "En marcha:", 'Sí' if self.en_marcha else 'No',)

# Crear dos objetos a partir de la clase Coche
coche1 = Coche("Toyota", "Corolla", 2020)
coche2 = Coche("Honda", "Civic", 2018)

# Usar algunos atributos y métodos
coche1.mostrar_info()
coche1.arrancar()
coche1.detener()



coche2.mostrar_info()
coche2.arrancar()
coche2.detener()

