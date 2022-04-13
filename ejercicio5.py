import random
numero = random.randint(1, 20)
contador = int(1)
i = int(0)

while i <1:
    print(numero)
    adivinar = int(input("Adivine el número del 1 al 20 "))
    if adivinar == numero:
        i=+1
    else:
        contador = contador + 1

print(f"Número de intentos = {contador}")
