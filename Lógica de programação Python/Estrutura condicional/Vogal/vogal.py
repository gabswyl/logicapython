# Faça um programa que verifique se uma letra digitada é vogal ou consoante

letter = str(input("Insira a sua letra para verificar se é vogal ou consoante: "))

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
  print("Essa letra é considerada como vogal")
else:
  print("Essa letra é considerada como consoante")
