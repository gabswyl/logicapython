# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário as quantidades de latas de tinta a serem compradas e o preço total.

metros = int(input('Metros: '))

if metros % 54 != 0:
    latas = int(metros / 54) + 1
else:
    latas = int(metros / 54)

valor = latas * 80

print('Uma lata está custando por', valor)