vocales = "aeiou" # Definimos las vocales que queremos contar

def contar_vocales(frase): # Esta función cuenta las vocales en una frase
    contador = 0
    frase = frase.lower() # Convertimos la frase a minúsculas para que no haya distinción entre mayúsculas y minúsculas
    for letra in frase:
        if letra in vocales:
            contador += 1 # Si la letra está en la lista de vocales, aumentamos el contador
    return contador 

while True: # Bucle infinito para pedir frases al usuario
    print("Escribe una frase (o escribe 'salir' para terminar):")
    frase = input()

    if frase.lower() == "salir":
        print("¡Hasta luego!")
        break  
    resultado = contar_vocales(frase) # Llamamos a la función contar_vocales con la frase introducida por el usuario
    print("la palabra tiene: ", resultado, "vocales") # Imprimimos el resultado