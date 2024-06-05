conjunto1 = {1, 2, 3, 4, 5, 6, 7}
conjunto2 = {2, 8, 9, 10, 11, 12, 3, 4, 5}
conjunto3 = {5, 6, 7, 13, 14, 15, 16, 2}

union = conjunto1 | conjunto2 | conjunto3

conjunto_pares = {valor for valor in union if valor % 2 == 0}

print(union)

print(conjunto_pares)