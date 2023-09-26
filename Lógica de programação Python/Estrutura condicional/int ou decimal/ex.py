# Faça um programa que peça um numero e informe se o numero é inteiro ou decimal.

import math

numero = float(input("Inisira o numero: "))
if math.floor(numero) == numero:
 print("O numero é inteiro ")
else:
 print("O numero é decimal")