preco = int(input("Digite a quantidade de notas: "))

#-----------------------------------------------------------#
centena = preco // 100

centenaR = preco % 100
#-----------------------------------------------------------#
cinquenta = centenaR // 50

cinquentaR = centenaR % 50
#-----------------------------------------------------------#
vinte = cinquentaR // 20

vinteR = cinquentaR % 20
#-----------------------------------------------------------#
dez = vinteR // 10

dezR = vinteR % 10
#-----------------------------------------------------------#
dois = dezR // 2

doisR = dezR % 2
#-----------------------------------------------------------#
um = doisR // 1
#-----------------------------------------------------------#

if centena > 0:
  print("Voçe precisa de {} notas de 100".format(centena))

if cinquenta > 0:
  print("Voçe precisa de {} notas de 50".format(cinquenta))

if vinte > 0:
  print("Voçe precisa de {} notas de 20".format(vinte))

if dez > 0:
  print("Voçe precisa de {} notas de 10".format(dez))

if dois > 0:
  print("Voçe precisa de {} notas de 2".format(dois))

if um > 0:
  print("Voçe precisa de {} notas de 1".format(um))
