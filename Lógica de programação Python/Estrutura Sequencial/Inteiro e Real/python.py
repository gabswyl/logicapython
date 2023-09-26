# 11 - Faça um programa que peça 2 números inteiros e um número real. calcule e mostre:
# a. produto do dobro do primeiro com metade do segundo
# b. a soma do triplo do primeiro com terceiro
# c. o terceiro elevado ao cubo

numeroInteiro = int(input('insira seu numero inteiro: '))
numeroInteiro2 = int(input('insira seu numero inteiro: '))
numeroReal = float(input('Insira seu numero real: '))

print ('A:', ((2*numeroInteiro) * (numeroInteiro/2)))
print ('B:', (3 * numeroInteiro) + numeroReal)
print ('C:', numeroReal**3)

