i = int(1)
suma = int(0)

while i == 1:
    numero = int(input("Digite un numero, para terminar el proceso ponga (0) "))
    if numero == 0:
        i+=1
    else:
        suma = suma + numero




print(f"La suma de los números es de {suma} y la media es de {suma/2}")
