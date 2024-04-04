from random import randint
from time import sleep

natural = [7, 11]
craps = [2, 3, 12]
ponto = [4, 5, 6, 8, 9, 10]

rodada = 0

while True:
  rodada += 1
  print("-" * 10)
  print(f"{rodada}º Rodada")
  print("-" * 10)

  sleep(2)

  primeiro_dado = randint(1, 6)
  segundo_dado = randint(1, 6)


  soma_dos_dados = primeiro_dado + segundo_dado
  print(f"A soma dos dados é igual a {soma_dos_dados}")
  print("-"*10)



  sleep(2)

  if rodada == 1: 
    if soma_dos_dados in natural:
      print("Natural! O jogador venceu!")
      break
    elif soma_dos_dados in craps:
      print("Craps! O jogador perdeu!")
      break    
    else:
      print("Ponto! O jogador terá outro rodada!")

  else: 
    if soma_dos_dados == 7:
      print("\033[31;1mDerrota! O jogador tirou o número 7\033[m")
      break
    elif soma_dos_dados in ponto:
      print("\033[32;1mVitória!\033[m")
      break

  sleep(2)




