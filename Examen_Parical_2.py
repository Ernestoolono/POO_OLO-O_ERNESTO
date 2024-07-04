class Motor:
    def __init__(self, tipo, cilindrada):
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.temperatura = 0
        self.encendido = False

    def encender(self):
        self.encendido = True
        self.temperatura = 30
        print("El motor de ", self.tipo, "se ha encendido.")

    def apagar(self):
        self.encendido = False
        self.temperatura = 0
        print("El motor de ", self.tipo, "se ha apagado.")

    def mostrar_info(self):
        print("Tipo de motor:", self.tipo, ", Cilindrada:", self.cilindrada, "cc, Temperatura:", self.temperatura, "°C, Encendido:", "Sí" if self.encendido else "No")

class Coche:
    def __init__(self, marca, modelo, año, tipo_motor, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = Motor(tipo_motor, cilindrada)  # Composición
        self.en_marcha = False
    
    def arrancar(self):
        self.motor.encender()
        self.en_marcha = True
        print("El coche", self.marca, self.modelo, "ha arrancado.")
    
    def detener(self):
        self.motor.apagar()
        self.en_marcha = False
        print("El coche", self.marca, self.modelo, "se ha detenido.")
    
    def mostrar_info(self):
        print("Marca:", self.marca, ", Modelo:", self.modelo, ", Año:", self.año, ", En marcha:", "Sí" if self.en_marcha else "No")
        print("Información del motor:")
        self.motor.mostrar_info()

    def tiene(self, Llantas):
        print(self.modelo, "Tiene llantas de tipo", Llantas.Tipo)


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
            print(self.nombre, "tiene un", coche.marca, coche.modelo, "en su inventario.")

    def mostrar_inventario(self):
        print("Inventario de", self.nombre, ":")
        for coche in self.inventario:
            coche.mostrar_info()

    def mostrar_clientes(self):
        print("Clientes de", self.nombre, ":")
        for cliente in self.clientes:
            print("-", cliente.nombre, "(Teléfono:", cliente.telefono, ")")

class Potencia_Maxima(Coche):
    def __init__(self, marca, modelo, año, motor, maxima_velocidad):
        super().__init__(marca, modelo, año, motor, cilindrada=120)
        self.maxima_velocidad = maxima_velocidad

    def de_0_a_100(self):
        print(self.marca, "Avanza de 0 a 100 en: ", self.maxima_velocidad)

class Llantas:
    def __init__(self, Tipo, Libras):
        self.Tipo = Tipo
        self.Libras = Libras

    def describir(self):
        print("Es de tipo", self.Tipo,  "y soporta: ", self.Libras, "Estas libras")

class Interior(Coche):
    def __init__(self, marca, modelo, año, motor, cilindrada, interior, color ):
        super().__init__(marca, modelo, año, motor, cilindrada)
        self.color_interior = color
        self.tipo_interior = interior

    def color_int(self):
        print(self.marca, "Es de color: ", self.color_interior, " y tiene un interior de tipo: ", self.tipo_interior)

class Transmicion(Coche):
    def __init__(self, marca, modelo, año, motor, cilindrada, transmicion):
        super().__init__(marca, modelo, año, motor, cilindrada)
        self.transmicion = transmicion

    def tipo_transmicion(self):
        print(self.marca, "Tiene una transmicion de tipo: ", self.transmicion)


# Crear objetos

coche1 = Coche("Toyota", "Corolla", 2020, "Gasolina", 1800)
coche2 = Coche("Honda", "Civic", 2018, "Híbrido", 1500)
coche3 = Coche("Ford", "Mustang", 2022, "Gasolina", 5000)
coche4 = Coche("Lamborghini", "huracan performante", 2024, "Gasolina", 120)
coche5 = Coche("Ferrari", "458 Spyder", 2023, "Gasolina", 110)

dueño1 = Dueño("Carlos", "61282625262")
dueño2 = Dueño("Angel", "61485423262")

concesionario = Concesionario("AutoMax")

maxima_potencia = Potencia_Maxima("Lamborghini", "huracan performante", 2024, "Gasolina", 120)
maxima_potencia1 = Potencia_Maxima("Ferrari", "458 Spyder", 2023, "Gasolina", 110)

Llantas1 = Llantas("Carretera", 167)
Llantas2 = Llantas("Nieve", 268)

colorint1 = Interior("Ferrari", "488 Spider", 2025, "Hibrido", 2600, "Alcantara", "Rojo lava")
colorint2 = Interior("Lamborghini", "SVJ Roadster", 2023, "Gasolina", 3500, "Piel", "Morado")

Transmicion1 = Transmicion("Ferrari", "488 Spider", 2025, "Hibrido", 2600, "Automatica")
Transmicion2 = Transmicion("Lamborghini", "SVJ Roadster", 2023, "Gasolina", 3500, "Automatica")

# Usar la asociación y composición
concesionario.agregar_coche(coche1)
concesionario.agregar_coche(coche2)
concesionario.agregar_coche(coche3)
concesionario.agregar_coche(coche4)
concesionario.agregar_coche(coche5)



while True:

    print("¿Que quieres hacer el dia de hoy en AutoMax?")

    print("A)  Observar el inventario de AutoMax")
    print("B)  Comprar un coche")
    print("C)  Clientes que rentaron un Coche")
    print("D)  Observar el tipo de Autos con tipos de color y tipo de interiores")
    print("E)  Vender un auto")
    print("F)  Potencia maxima de autos")
    print("G)  Tipos de transmiciones")
    print("H)  Tipos de Llantas")
    print("I)  Especificaciones de vehiculos")
    print("K)  Salir")

    menu = input("ingresa la opcion: ")

    if menu == "A":
        print(concesionario.mostrar_inventario())

    elif menu == "B":
        print(Coche.mostrar_info(coche1), Coche.mostrar_info(coche2), Coche.mostrar_info(coche3), 
              Coche.mostrar_info(coche4), Coche.mostrar_info(coche5))

    elif menu == "C":
        print(dueño1.rentar_carros(coche5))

    elif menu == "D":
        print(colorint1.color_int(), colorint2.color_int())

    elif menu == "E":
        print(concesionario.vender_coche(coche1, dueño1), concesionario.vender_coche(coche2, dueño2))

    elif menu == "F":
        print(maxima_potencia.de_0_a_100(), maxima_potencia1.de_0_a_100())

    elif menu == "G":
        print(Transmicion2.tipo_transmicion(), Transmicion1.tipo_transmicion())

    elif menu == "H":
        print(coche1.tiene(Llantas1), coche2.tiene(Llantas2), coche3.tiene(Llantas1), 
              coche4.tiene(Llantas2), coche5.tiene(Llantas2))

    elif menu == "I":
        print(coche5.arrancar(), coche5.mostrar_info(), coche5.detener())

    elif menu == "K":
        print("Sliendo del Programa")
        
        break
 
    else:
        print("Opcion no valida, seleccione de nuevo")

