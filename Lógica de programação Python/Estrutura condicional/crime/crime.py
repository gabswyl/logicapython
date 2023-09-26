# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. as perguntas são:
# a) telefonou para vitima? b) esteve no local do crime? c) mora perto da vitima? d) devia para vitima e) ja trabalhou com a vitima?
# o programa deve no final emitir uma classificacao sobre a participacao da pessoa no crime.
# se a pessoa responder positivamente a 2 questoes ela deve ser classificada como susp, entre 3 e 4 como cumplica e 5 como assasino, caso contrario como inocente

print("Responda as perguntas respondendo sim ou não: ")
primeiraPergunta = str(input("Telefonou para vitima? sim ou não " ))
segundaPergunta = str(input("Esteve no local do crime? sim ou não "))
terceiraPergunta = str(input ("Mora perto da vitima? sim ou não "))
quartaPergunta = str(input("Você devia para vitima? sim ou não "))
quintaPergunta = str(input("Você já trabalhou com a vitima? sim ou não "))

valor = 0


if primeiraPergunta == "sim":
  valor += 1
if segundaPergunta == "sim":
  valor += 1
if terceiraPergunta == "sim":
  valor += 1
if quartaPergunta == "sim":
  valor += 1
if quintaPergunta == "sim":
  valor += 1


if valor == 2:
 print("Você é SUSPEITO!")
elif valor >= 3 and valor <= 4:
 print("Você é CUMPLICE!")
elif valor == 5:
 print("Você é Assasino!")
else:
 print("Você é inocente!")

