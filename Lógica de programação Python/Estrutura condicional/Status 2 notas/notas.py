# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete:
# - A mensagem "Reprovado", se a média for menor que sete:
# - A mensagem "Aprovado com distinção", se a média for igual a dez

notaAluno = float(input("Insira sua primeira nota: "))
segundaNota = float(input("Insira sua segunda nota: "))

calcNotas = (notaAluno + segundaNota) / 2
resultado = calcNotas

if resultado >= 7:
  print("Parabéns! Você foi aprovado")
elif resultado == 10:
  print("Parabéns! Você foi aprovado com distinção")
else:
    print("Infelizmente! Você foi reprovado.")