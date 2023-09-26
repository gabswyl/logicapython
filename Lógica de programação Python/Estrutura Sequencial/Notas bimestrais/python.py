# 4 - Faça um programa que peça as 4 notas bimestrais e mostre a média

primeiraNota = float(input("insira a sua primeira nota do bimestre: "))
segundaNota = float(input("insira a sua segunda nota do bimestre: "))
terceiraNota = float(input("insira a sua terceira nota do bimestre: "))
quartaNota = float(input("insira a sua quarta nota do bimestre: "))


calcSoma = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 2
print(calcSoma)