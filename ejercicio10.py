numero = int(input("Digite un número para determinar si es primo o no "))
if numero > 1:
    for i in range(2, int(numero/2)+1):
        if (numero % i) == 0:
            print("No es primo")
            break
    else:
        print("Es primo")

else:
    print("No es primo")
