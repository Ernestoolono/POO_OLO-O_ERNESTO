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
        print("Marca:", self.marca, "Modelo:", self.modelo, "Año:", self.año, "En marcha:" , 'Sí' if self.en_marcha else "No")

class Dueño:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.carros = []

    def comprar_carros(self, carro):
        self.carros.append(carro)
        print(self.nombre, "Teléfono:", self.telefono, "ha comprado un", carro.marca, carro.modelo)

    def vender_carros(self, carro):
        if carro in self.carros:
            self.carros.remove(carro)
            print(self.nombre, "está vendiendo un", carro.marca, carro.modelo)
        else:
            print(self.nombre, "no tiene un", carro.marca, carro.modelo, "para vender")

    def rentar_carros(self, carro):
        if carro in self.carros:
            print(self.nombre, "está rentando un", carro.marca, carro.modelo)
        else:
            print(self.nombre, "no tiene un", carro.marca, carro.modelo, "para rentar")

# Crear dos objetos a partir de la clase Coche
coche1 = Coche("Toyota", "Corolla", 2020)
coche2 = Coche("Honda", "Civic", 2018)

# Crear tres objetos a partir de la clase Dueño
carro1 = Dueño("Carlos", "61282625262")
carro2 = Dueño("Angel", "61485423262")
carro3 = Dueño("Yamir", "61527282636")

# Usar algunos atributos y métodos
coche1.mostrar_info()
coche1.arrancar()
coche1.detener()

coche2.mostrar_info()
coche2.arrancar()
coche2.detener()

# Primero, los dueños deben comprar los coches antes de poder venderlos o rentarlos
carro2.comprar_carros(coche1)
carro3.comprar_carros(coche2)

# Ahora pueden vender o rentar
carro2.vender_carros(coche1)
carro3.rentar_carros(coche2)