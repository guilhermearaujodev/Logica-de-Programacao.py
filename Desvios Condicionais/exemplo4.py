#Dado um número pelo usuário, exibir o dia da semana correspondente. 
dia = int(input("Digite um número: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else: 
    print("Dia inválido.")