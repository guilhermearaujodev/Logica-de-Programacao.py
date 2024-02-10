#Laço Pré-condicional
#Solicitar ao usuário que digite S para sim ou N para não obrigatoriamente.
#Se digitar uma letra que não for S ou N, realizar a repetição.
#while = enquanto
opcao = input("Digite [S]im ou [N]ão: ")
while opcao != 's' and opcao != 'S' and opcao != 'n' and opcao != 'N':
    print("Você digitou ", opcao, "digite S ou N!")
    opcao = input("Digite [S]im ou [N]ão: ")

print("Você digitou ", opcao)