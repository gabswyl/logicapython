# Faça um programa que leia três numeros e mostre-os em ordem decrescente


primeiroNumero = float(input("Primeiro numero: "))
segundoNumero = float(input("Segundo numero: "))
terceiroNumero = float(input("Terceiro numero: "))

if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    if segundoNumero > terceiroNumero:
        print("Ordem: {}, {} e {}".format(primeiroNumero, segundoNumero, terceiroNumero))
    else:
        print("Ordem: {}, {} e {}".format(primeiroNumero, terceiroNumero, segundoNumero))
elif segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    if primeiroNumero > terceiroNumero:
        print("Ordem: {}, {} e {}".format(segundoNumero, primeiroNumero, terceiroNumero))
    else:
        print("Ordem: {}, {} e {}".format(segundoNumero, terceiroNumero, primeiroNumero))
elif terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
    if primeiroNumero > segundoNumero:
        print("Ordem: {}, {} e {}".format(terceiroNumero, primeiroNumero, segundoNumero))
    else:
        print("Ordem: {}, {} e {}".format(terceiroNumero, segundoNumero, primeiroNumero))
else:
    print("Os números são iguais.")
