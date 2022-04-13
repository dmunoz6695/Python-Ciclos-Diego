cantidad = int(input("Digite el número de veces que se va a introducir un número "))
count1 = int(0)
count2 = int(0)
count3 = int(0)
for i in range (cantidad):

    numero = int(input("Digite un número "))
    if numero > 0:
        count1 = count1 + 1
    elif numero <0:
        count2 = count2 + 1
    else:
        count3 = count3 + 1

print(f"Hay {count1} números mayores a 0, hay {count2} números menores a 0, y hay {count3} números iguales a 0 ")

