KG = int(input("Ingrese el numero de kilogramos que desea enviar: "))

if KG <= 1:
    print("$50")

elif KG <= 5:
    print("$100")

elif KG <= 10:
    print("$200")

elif KG >= 10:
    print("$500")

else:
    print("No se puede enviar")
