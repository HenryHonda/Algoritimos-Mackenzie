a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if b > a:
    temp = a
    a = b
    b = temp

if c > a:
    temp = a
    a = c
    c = temp

#As trocas foram feitas para ter certeza que A sempre vai ser a hipotenusa (no caso o lado maior do trinagulo)

if a**2 != b**2 + c**2:
    print("Triangulo nao retangulo!")
else:
    print("Triangulo retangulo!")