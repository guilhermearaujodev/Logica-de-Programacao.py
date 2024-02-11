#Laço Para
#Dados 5 números pelo usuário, exibir o de maior valor.
num = int(input("Digite 5 números: "))
maior = num
for const in range(1, 5, 1):
    num = int(input())
    if num > maior:
        maior = num
print("Maior valor = ", maior)
