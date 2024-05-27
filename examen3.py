Edades = [12, 7, 8, 9, 23, 35, 46, 35, 19, 24, 45, 45, 12, 6, 3, 67]
Infancia = []
Adolecentes = []
Jóvenes = []
Adultos = []

for numeros in Edades:
    if numeros >= 6 and numeros <= 11:
        Infancia.append(numeros)
    elif numeros >= 12 and numeros <= 17:
        Adolecentes.append(numeros)
    elif numeros >= 18 and numeros <= 26:
        Jóvenes.append(numeros)
    elif numeros > 27:
        Adultos.append(numeros)

print("Edades: ", Edades)
print("Infancia: ", Infancia)
print("Adolecentes: ", Adolecentes)
print("Jóvenes: ", Jóvenes)
print("Adultos: ", Adultos)
