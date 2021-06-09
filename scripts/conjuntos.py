
# numeros = {1, 2, 3, 3, 4, 4, 5}
# print(type(numeros))
# print(numeros)

# numeros = [10, 1, 2, 3, 3, 4, 4, 5, "rafael", "rafael", "galleani", "galleani"]
# numeros = list(set(numeros))
# print(numeros)

conjunto1 = {10, 20, 30, 40} 
conjunto2 = {30, 40, 50, 60}

print(conjunto1.union(conjunto2))
print(conjunto1.intersection(conjunto2))

print(conjunto1.difference(conjunto2))

print(conjunto1.symmetric_difference(conjunto2))

