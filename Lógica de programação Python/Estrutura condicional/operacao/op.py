# Faça um programa que leia 2 numero e em seguida pergunte ao usuário qual operação que ele deseja realizar.
# O resultado da operação deve ser acompahanhado de uma frase que diga se o numero é: a) par ou impar, b) positivo ou negativo,  c) int ou decimal

import math

primeiroNumero = float(input("Insira 1° numero: "))
segundoNumero = float(input("Insira 2° numero: "))

operacao = str(input("Você deseja utilizar multiplicacao, divisao, soma ou subtracao?: "))

if operacao == "multiplicacao":
 calc = primeiroNumero * segundoNumero
elif operacao == "divisao":
 calc = primeiroNumero / segundoNumero
elif operacao == "soma":
 calc = primeiroNumero + segundoNumero
elif operacao == "subtracao":
 calc = primeiroNumero - segundoNumero
else:
 print("Operação não encontrada! Escreva a palavra corretamente de acordo com texto")


if calc % 2:
  print("Seu numero é impar")
else:
  print("Seu numero é par")


if calc > 0:
  print("Esse numero positivo")
else:
  print("Esse numero não é positivo")


if math.floor(calc) == calc:
 print("O numero é inteiro ")
else:
 print("O numero é decimal")
