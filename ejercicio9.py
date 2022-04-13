x = int(0)
while x < 1:
    numero = int(input("Digite un número para ver su tabla \n"))
    calculo = int(0)
    for i in range(12):
        i = i + 1
        calculo = numero * i
        print(f"{numero} multiplicado por {i} es = {calculo}")
        calculo = 0
    if i == 12:
        pregunta = int(input("Digite 1 si quiere ver la tabla de otro número, digite 0 para terminar \n"))
    if pregunta == 0:
        x += 1
    




