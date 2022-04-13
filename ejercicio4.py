cantidad = int(input("Digite la cantidad de veces que va a sumar "))
par = int(0) 
impar = int(0)

for i in range(cantidad):
    numero = int(input("Digite número a sumar sea par o impar "))
    if numero % 2 == 0:
        par = par + numero
    else:
        impar = impar + numero


print(f"La suma de los números pares son {par} y la suma de los números impares son {impar}")
