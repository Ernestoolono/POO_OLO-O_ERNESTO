num1 = int(input("Ingrese el Primer promedio: "))
num2 = int(input("Ingrese el Segundo promedio: "))
num3 = int(input("Ingrese el tercer promedio: "))

if num1 > num2 and num1 > num3:
  NumMayor = num1
elif num2 > num1 and num2 > num3:
  NumMayor = num2
else:
  NumMayor = num3
print("El numero mayor es: ", NumMayor)
