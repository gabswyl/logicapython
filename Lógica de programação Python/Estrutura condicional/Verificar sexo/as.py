# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, sexo inválido

sexo = str(input("Insira o seu sexo M ou F: "))

if sexo == "F":
  print("Você selecionou Feminino")
elif sexo == "M":
    print("Você selecionou Masculino")
else:
  print("Sexo inválido")