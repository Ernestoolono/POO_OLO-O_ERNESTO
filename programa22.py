def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        opcion = input("Ingresa la opción (1/2/3/4): ")
        
        if opcion in ['1', '2', '3', '4']:
            break
        else:
            print("Opción inválida. Por favor intenta de nuevo.")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif opcion == '2':
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif opcion == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcion == '4':
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")

if __name__ == "__main__":
    calculadora()
