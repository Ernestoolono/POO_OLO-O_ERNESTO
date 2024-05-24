while True:

 print("Bienvenido a la calculadora de Grados")

 print("¿Qué quieres calcular el dia de hoy?")

 print("A) Grados Fahrenheit a Celcius")
 print("B) Grados Celcius a Fahrenheit")
 print("C) Salir")

 menu = input("Ingresa la opcion: ") 

 if menu == "A":
  Fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
  Celcius = (Fahrenheit - 32 * 5 /9)
  print(Celcius)

 elif menu == "B":
  Celcius = float(input("Ingrese la temperatura en Grados Celcius: "))
  Fahrenheit = (Celcius * 5 /9 + 32)
  print(Fahrenheit)

 elif menu == "C":
  print("Sliendo del Programa")

  break
 
 else:
  print("Opcion no valida, seleccione de nuevo")