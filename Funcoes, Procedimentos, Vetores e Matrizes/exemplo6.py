#Funções com Parâmetros
#Criar uma função que retorne o maior entre dois números passados por parâmetros
def maior2n(num1, num2):
    if num1 > num2:
        maior = num1
    else: 
        maior = num2
    return maior

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
print("Maior número = ", maior2n(n1, n2))