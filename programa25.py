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
        print("Marca:", self.marca, ", Modelo:", self.modelo, ", Año:", self.año, ", En marcha:", 'Sí' if self.en_marcha else 'No')

class Dueño:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.carros = []

    def comprar_carros(self, carro):
        self.carros.append(carro)
        print(self.nombre, "(Teléfono:", self.telefono, ") ha comprado un", carro.marca, carro.modelo)

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

class Concesionario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.clientes = []

    def agregar_coche(self, coche):
        self.inventario.append(coche)
        print(self.nombre, "ha agregado un", coche.marca, coche.modelo, "a su inventario.")

    def vender_coche(self, coche, dueño):
        if coche in self.inventario:
            self.inventario.remove(coche)
            dueño.comprar_carros(coche)
            if dueño not in self.clientes:
                self.clientes.append(dueño)
            print(self.nombre, "ha vendido un", coche.marca, coche.modelo, "a", dueño.nombre)
        else:
            print(self.nombre, "no tiene un", coche.marca, coche.modelo, "en su inventario.")

    def mostrar_inventario(self):
        print("Inventario de", self.nombre, ":")
        for coche in self.inventario:
            coche.mostrar_info()

    def mostrar_clientes(self):
        print("Clientes de", self.nombre, ":")
        for cliente in self.clientes:
            print("-", cliente.nombre, "(Teléfono:", cliente.telefono, ")")

# Crear objetos
coche1 = Coche("Toyota", "Corolla", 2020)
coche2 = Coche("Honda", "Civic", 2018)
coche3 = Coche("Ford", "Mustang", 2022)

dueño1 = Dueño("Carlos", "61282625262")
dueño2 = Dueño("Angel", "61485423262")

concesionario = Concesionario("AutoMax")

# Usar la asociación
concesionario.agregar_coche(coche1)
concesionario.agregar_coche(coche2)
concesionario.agregar_coche(coche3)

concesionario.mostrar_inventario()

concesionario.vender_coche(coche1, dueño1)
concesionario.vender_coche(coche2, dueño2)

concesionario.mostrar_inventario()
concesionario.mostrar_clientes()

# Usar métodos de las clases originales
dueño1.rentar_carros(coche1)
dueño2.vender_carros(coche2)