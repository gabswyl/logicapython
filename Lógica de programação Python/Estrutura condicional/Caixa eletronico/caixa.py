# Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão de as 1, 5
# 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 Reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# a. ex1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# b. ex2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1


saque = int(input('Valor para sacar [10-600]: '))

if 10 <= saque <= 600:
    cem = int(saque / 100)
    saque = saque - (cem * 100)

    cinquenta = int(numero / 50)
    saque = saque - (cinquenta * 50)

    dez = int(numero / 10)
    saque = saque - (dez * 10)

    cinco = int(saque / 5)
    saque = saque - (cinco * 5)

    um = saque

    print("Você precisa de {} para nota de 1000".format(cem))
    print("Você precisa de {} para nota de 50".format(cinquenta))
    print("Você precisa de {} para nota de 10".format(dez))
    print("Você precisa de {} para nota de 5".format(cinco))
    print("Você precisa de {} para nota de 1".format(um))
else:
    print('O valor de saque deve estar entre 10 e 600.')