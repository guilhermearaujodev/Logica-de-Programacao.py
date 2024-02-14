#FUNÇÕES E PROCEDIMENTOS

#Em  uma  instituição  de  ensino, um  aluno  é  submetido  a  três  avaliações  em  um semestre. 

#A média semestral é calculada por meio de uma média simples das duas maiores avaliações obtidas entre três avaliações. 
#Caso essa média semestral resulte em uma nota inferior a 4, o aluno foi reprovado sem outra oportunidade. 
#Caso a média semestral seja maior ou igual a 7, o aluno foi aprovado de forma direta.
#Caso a média esteja entre 4 e 6.9, o aluno tem a oportunidade de fazer o exame por meio de uma nova avaliação.
#Considerando que o aluno está em exame, média final é uma média simples da média semestral com a nota da avaliação obtida no exame. 
#Caso a média final seja inferior a 5, o aluno foi Reprovado em Exame, senão ele foi aprovado.

#Requisitos:
#-O algoritmo efetua todo esse cálculo com apenas um aluno.
#-Consistir as notas para que estejam entre 0 e 10.
#-As mensagens informativas devem ser claras em relação ao problema ou à situação do aluno.
#-Quando necessário, exibir as médias calculadas para simples conferência

nota1 = float(input("Nota 1: "))
#verificação se a nota é válida
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        nota3 = float(input("Nota 3: "))
        if nota3 >= 0 and nota3 <= 10:
        #Verificação da menor entre 3 notas
            menor_nota = nota1
            if nota2 < menor_nota:
                menor_nota = nota2
            if nota3 < menor_nota:
                menor_nota = nota3

#Cálculo da média semestral com as duas notas maiores
            media_semestral = (nota1 + nota2 + nota3 - menor_nota) / 2
            print(f"A sua média semestral é {media_semestral:.1f}")
            #verificação do status de aprovação ou não do aluno
            if media_semestral < 4:
                print("Você está reprovado direto.")                    
            elif media_semestral >= 7:
                print("Você está aprovado direto.")
            else:
                #caso o aluno tenha ficado em exame
                print("\nVOCê FICOU EM EXAME\n")
                nota_exame = float(input("Digite a nota do exame: "))
                if nota_exame >= 0 and nota_exame <= 10:
                    media_exame = (media_semestral + nota_exame) / 2 
                    #status de aprovação ou não do aluno após o exame
                    if media_exame < 5:
                        print(f"\nReprovado em exame com média {media_exame:.1f}\n")
                    else:
                        print(f"\nAprovado em exame com média {media_exame:.1f}\n")
                else:
                    print(f"Nota de exame {nota_exame} inválida!")
        else:
            print(f"Nota 3: {nota3} -É inválida!")
    else:
        print(f"Nota 2: {nota2} - É inválida!")
else:
    print(f"Nota 1 {nota1} - É inválida!")