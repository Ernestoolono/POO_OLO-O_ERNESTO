while True:
    print("¿Qué Area de figura desea calculra?")
    print("A) Cuadrado")
    print("B) Triangulo")
    print("C) Rectángulo")
    print("D) Salir")

    Menu = input("Ingrese la opción: ")

    if Menu == "A":
       lado1 = int(input("Ingrese el lado 1 del cuadrado: "))
       lado2 = int(input("Ingrese el lado 2 del cuadrado: "))
       cuadrado = lado1 * lado2
       print(cuadrado)

    elif Menu == "B":
        Base1 = float(input("Ingrese la Base del Triangulo: "))
        Altura1 = float(input("Ingrese la Altura del Triangulo: "))
        Triangulo = Base1 * Altura1 / 2
        print(Triangulo)

    elif Menu == "C":
        Base2 = int(input("Ingrese la base del rectangulo: "))
        Altura2 = int(input("Ingrese la Altura del Rectangulo: "))
        Rectangulo = Base2 * Altura2
        print(Rectangulo)

    elif Menu == "D":
        print("Saliendo del Programa")
        break
    else:
        print("Seleccione una opcion correcta")
