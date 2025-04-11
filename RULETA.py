import random
nombres = ["Alice", "Bob", "Charlie", "David", "Eve"]
print ("Bienvenido a la ruleta rusa")
print ("presiona enter para empezar")

while True:
    entrada = input("Presiona Enter para girar: ")
    if entrada.lower () == "salir":
        print ("Bai bai")
        break

    ganador = random.choice(nombres)
    print ("El ganador es", ganador)