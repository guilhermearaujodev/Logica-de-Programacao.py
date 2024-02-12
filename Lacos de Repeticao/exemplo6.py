#Laço Para
#Dados 10 números pelo usuário, somá-los e, no final, exibir a somatória.
soma = 0
print("Digite 10 números: ")

#Laço configurado para 10 voltas 
for i in range(1, 11, 1):
    n = float(input())
    soma = soma + n

print("Somatória = ", soma)