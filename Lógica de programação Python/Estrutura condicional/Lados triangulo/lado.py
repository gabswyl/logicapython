# # Faça um programa que peça os 3 lados de um triangulo. O programa deverá informar
# se os valores podem ser um triangulo. Indique, caso os lados formem um triangulo. se o mesmo é:
# equilatero, isosceles ou escaleno

primeiroLado = float(input("Insira o primeiro lado: "))
segundoLado = float(input("Insira o segundo lado: "))
terceiroLado = float(input("Insira o terceiro lado: "))

if primeiroLado == segundoLado and segundoLado == terceiroLado:
  print("Lados podem formar um triangulo")
  print("Tipo equilatero: 3 lados iguais")
elif primeiroLado == segundoLado or segundoLado == terceiroLado or primeiroLado == terceiroLado:
  print("Lados podem formar um triangulo")
  print("Tipo Isoceles: 2 lados iguais")
else:
  print("Lados podem formar um triangulo")
  print("Tipo Escaleno: 3 lados diferentes")