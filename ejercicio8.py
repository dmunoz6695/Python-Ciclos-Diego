y = input("Digite un numero ")
x = int(y)
count = 1
z = 1
while z <= x:
    count = count * z
    z = z + 1
print(f"El factorial del numero digitado es {count}")