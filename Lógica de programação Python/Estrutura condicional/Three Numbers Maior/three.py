# Faça que leia três numero e mostre o maior deles

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