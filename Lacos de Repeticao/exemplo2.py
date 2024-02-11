#Laço Enquanto-faça
#Fazer um algoritmo que leia e some diversos números dados pelo usuário.
# Quando o usuário digitar 0, finaliza o algoritimo. No final, exibe a soma resultante.
print("Digite 0 para finalizar")
soma = 0
num = 1

while num != 0:
    num = float(input("Digite um número: "))
    soma = soma + num

print("Somatória = ", soma)