import math

custo = float(input("Digite o custo total do espetaculo: "))
ingresso = float(input("Digite o preco do ingersso: "))

lucro = float((custo * 1.23) / ingresso)

print("Para que o custo do espetaculo seja alcancado, devem ser vendidos pelo menos {} convites".format(int(custo / ingresso)))
print("Para obter um lucro de 23%, serao necessarios {} convites".format(math.ceil(lucro)))
