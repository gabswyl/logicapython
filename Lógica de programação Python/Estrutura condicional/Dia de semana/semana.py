# Faça um programa que leia um numero e exiba o dia correspondente da semana (domingo, segunda etc) gitar outr
# se digitar outro valor deve aparecer valor invalido

numerodoDia = float(input("Insira o dia da semana: "))

if numerodoDia == 1:
  print("Hoje é segunda feira! Espero que seu final de semana tenha sido incrivel")
elif numerodoDia == 2:
  print("Hoje é terça-feira! #Dia de estudo e trabalhos")
elif numerodoDia == 3:
 print("Hoje é quarta-feira! #Dia de estudo e trabalhos")
elif numerodoDia == 4:
 print("Hoje é quinta feira! Ufa, esta chegando final de semana")
elif numerodoDia == 5:
 print("Sextou! Irei planejar os planos de final de semana em ação!")
elif numerodoDia == 6:
  print("Sabadou! Hoje é dia de ir na festa com amigas ")
elif numerodoDia == 7:
  print("Domingou! Dia de ressaca!!!")
else:
  print("Dia inválido, tente novamente!")
