# Faça um programa que leia três numeros e mostre o maior e menor deles


primeiroNumero = float(input("Primeiro numero: "))
segundoNumero = float(input("Segundo numero:"))
terceiroNumero = float(input("Terceiro numero:"))


if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
  print("Esse é o maior numero: {} ".format(primeiroNumero))
elif segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
  print("Esse é o maior numero: {} ".format(segundoNumero))
elif terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
  print("Esse é o maior numero: {} ".format(terceiroNumero))
else:
 print("Todos numeros são iguais")


if primeiroNumero < segundoNumero and primeiroNumero < terceiroNumero:
  print("Esse é o menor numero: {} ".format(primeiroNumero))
elif segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
  print("Esse é o menor numero: {} ".format(segundoNumero))
elif terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
  print("Esse é o menor numero: {} ".format(terceiroNumero))
else:
 print("Todos numeros são iguais")
