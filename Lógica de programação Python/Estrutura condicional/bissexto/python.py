# Faça um programa que peça um numero correswpondente um determinado ano e em seguida informe
# se este ano é ou não bissexto.

anoBissexto = float(input("Insira o ano: "))

if anoBissexto % 400 == 0:
    print("O ano é bissexto")
elif anoBissexto % 4 == 0 and anoBissexto % 100 != 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

