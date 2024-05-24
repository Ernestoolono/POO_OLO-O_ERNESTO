lista = [15, 15, 45, 34, 12, 18, 20, 5, 6]
lista_menor = []
lista_mayor = []

for numeros in lista:
    if numeros < 18:
        lista_menor.append(numeros)
    else:
        lista_mayor.append(numeros)

print("lista de edades", lista)
print("lista de menores: ", lista_menor)
print("lista de mayores: ", lista_mayor)