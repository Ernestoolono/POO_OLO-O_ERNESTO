while True:

 print("Bienvenido a la informacion de funciones")

 print("¿Qué función quires conocer?")

 print("A) Abstracción")
 print("B) Encapsulamiento")
 print("C) Herencia")
 print("D) Polimorfismo")
 print("E) Salir")

 menu = input("Ingresa la opcion: ") 

 if menu == "A":
  Abstracción = (" La abstracción en la programación orientada a objetos (POO) es un concepto fundamental y se refiere a la capacidad de un lenguaje de programación para representar y manipular conceptos abstractos en el código. En PHP, la abstracción se logra a través de la creación de clases y la implementación de métodos y propiedades que representan las características y comportamientos de un concepto abstracto ")
  print(Abstracción)

 elif menu == "B":
  Encapsulamiento = ("En la Programación orientada a objetos (POO), la encapsulación se refiere a la agrupación de datos con los métodos que operan en esos datos, o la restricción del acceso directo a algunos de los componentes de un objeto")
  print(Encapsulamiento)

 elif menu == "C":
  Herencia = ("En programación orientada a objetos, la herencia es, después de la agregación o composición, el mecanismo más utilizado para alcanzar algunos de los objetivos más preciados en el desarrollo de software como lo son la reutilización y la extensibilidad.")
  print(Herencia)
 
 elif menu == "D":
  Polomorfismo = ("El polimorfismo es la capacidad de un objeto para adquirir múltiples formas o comportamientos. Volviendo a nuestra analogía LEGO, es como tener una pieza que puede encajar en varios lugares o tener varios usos según el contexto. ")
  print(Polomorfismo)
 
 elif menu == "E":
  print("Sliendo del Programa")

  break
 
 else:
  print("Opcion no valida, seleccione de nuevo")