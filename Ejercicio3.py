# Crear la lista de números
numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]

# Inicializar listas para almacenar números pares e impares
pares = []
impares = []

# Clasificar los números como pares e impares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Imprimir la salida en el formato deseado
print("Pares:", pares)
print("Impares:", impares)