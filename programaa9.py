contraseña_correcta = "POO123"

while True:
    contraseña = input("Ingrese su contraseña: ")

    if contraseña == contraseña_correcta:
        print("Acceso Autorizado")

        break

    else:
        print("Contraseña Incorrecta")
