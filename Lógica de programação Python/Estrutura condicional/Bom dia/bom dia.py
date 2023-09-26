
from ast import MatMult
# Faça um programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V - Vespertino ou N - Noturno.
# Imprima a mensagem "Bom dia!", "Boa tarde!" ou "Boa noite!" ou "Valor inválido"

turno = str(input("Você estuda em qual desses turnos matutino ou vespertino ou noturno? "))

if turno == "matutino":
  print("Bom dia!")
elif turno == "vespertino":
    print("Boa tarde!")
elif turno == "noturno":
    print("Boa noite!")
else:
  print("Valor inválido")