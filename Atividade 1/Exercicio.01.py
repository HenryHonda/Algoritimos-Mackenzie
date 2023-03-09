tempo = int(input("Digite a duracao do evento em segundos: "))

minutos = tempo // 60
horas = minutos // 60
segundos = tempo % 60

while minutos >= 60:
  minutos = minutos - 60

if segundos >= 60:
  segundos = segundos - (minutos * 60)

print("O evento durou {} horas {} minutos e {} segundos".format(
  horas, minutos, segundos))
