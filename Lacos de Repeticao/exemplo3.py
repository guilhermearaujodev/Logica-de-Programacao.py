#Laço Faça-enquanto
#Somar números digitados pelo usuário até que ele digite um número negativo.
#(O número negativo não deve fazer parte da soma)
soma = 0

while True:
    num = int(input("Digite um número: "))
    if num > 0:
        soma = soma + num
    else:
        break

print("Soma = ", soma)