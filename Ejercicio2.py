def contar_vocales(frase):
    # Convertir la frase a minúsculas para evitar problemas de coincidencia
    frase = frase.lower()
    
    # Inicializar un diccionario para contar las vocales
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Contar las vocales en la frase
    for letra in frase:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
    
    # Imprimir el resultado
    print("Escribe una frase:", frase)
    for vocal, cantidad in conteo_vocales.items():
        print(vocal, cantidad)

# Solicitar una frase al usuario
frase_usuario = input("Escribe una frase: ")

# Llamar a la función para contar las vocales
contar_vocales(frase_usuario)