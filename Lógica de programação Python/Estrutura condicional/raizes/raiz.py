# faça um programa que calcule as raizes de uma equação de segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências. Informando o usuario na seguinte situacoes
# a. Se usuario informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
# pedir os demais valores, sendo encerrado:
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa
# c. Se o delta calculado for igual a zero a equação apenas possui apenas uma raiz real: informe-a ao usuario
# d. se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuario:

import math

a = float(input("primeiro valor: "))
b = float(input("segundo valor: "))
c = float(input("terceiro valor: "))

equacaoDelta = b**2 - 4*a*c

if a == 0:
  print("Não é possível fazer equação de segundo grau começando com 0, programa encerrado")
elif equacaoDelta <= 0:
  print("A equação não possui raízes reais! Programa encerrado")
elif equacaoDelta == 0:
  verificarZero = -b / (2*a)
  print("A equação possui somente uma raiz real", verificarZero)
else:
   primeiroRaiz = (-b + math.sqrt(equacaoDelta)) / (2*a)
   segundoRaiz = (-b - math.sqrt(equacaoDelta)) / (2*a)
   print("A equação possui dois raizes: {}, {}.".format(primeiroRaiz, segundoRaiz))