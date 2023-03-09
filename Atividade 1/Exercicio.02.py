import math

n1 = float(input("Digite o comprimento de um dos catetos: "))
n2 = float(input("Digite o comprimento do outro cateto: "))

h = n1**2 + n2**2
hf = math.sqrt(h)

print("O valor da hipotenusa vale: {:.2f} ".format(hf))
