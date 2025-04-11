import random
numero_secreto = random.randint(1, 10)
while True:
    intento = input("Adivina el número entre 1 y 10: ")
    if not intento.isdigit():
        print("Por favor, introduce un número válido.")
        continue
    intento = int(intento)
    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")