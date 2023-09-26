#Faça um programa que peça dois números e imprima o maior deles

numeroUm = float(input('Insira o primeiro numero: '))
numeroDois = float(input('Insira o segundo numero: '))

if numeroUm > numeroDois:
  print("O numero {} é o maior que {}".format(numeroUm, numeroDois))
else:
    print("O numero {} é maior que {}".format(numeroDois, numeroUm))