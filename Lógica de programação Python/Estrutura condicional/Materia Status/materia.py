# Faça um programa que lê duas notas parciais obtidas por um aluno numa dispolicina ao longo de um
# semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Media de aproveitamento - Conceito
# Entre 9 e 10 - A APROVADO
# Entre 7.5 e 9.0 - B APROVADO
# Entre 6.0 e 7.5 - C  APROVADO
# Entre 4.0 e 6.0 - D  (REPROVADO)
# Entre 4.0 e zero - E (REPROVADO)

# O algoritmo deve mostrar na tela as notas, a média, o conceito corrrespondente e a mensagem aprovado
# se o conceito for a, b ou c ou reprovado for d ou e

notadoAluno1 = float(input("Insira a sua nota do trabalho em Algebra Linear: "))
notadoAluno2 = float(input("Insira a sua nota da prova em Algebra Linear: "))

calcMedia = (notadoAluno1 + notadoAluno2) / 2

if calcMedia > 9:
 print("Parabéns! Você foi aprovado em Algebra Linear. NOTA A")
elif calcMedia > 7.5:
 print("Parabéns! Você foi aprovado em Algebra Linear. NOTA B")
elif calcMedia > 6.0:
 print("Parabéns! Você foi aprovado em Algebra Linear. NOTA C")
elif calcMedia > 4.0:
 print("Infelizmente, você foi aprovado em Algebra Linear. NOTA D")
elif calcMedia < 4.0:
 print("Infelizmente, você foi aprovado em Algebra Linear. NOTA E")