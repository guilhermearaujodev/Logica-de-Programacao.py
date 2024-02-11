#LAÇO FAÇA-ENQUANTO
#Em uma eleição, há três candidatos: 1 – Huguinho; 2 – Zezinho e 3 – Luizinho. 
#Fazer um algoritmo que leia votos dados pelo usuário até que ele digite 0 (zero). 
#Ao finalizar a votação, informar quantos votos cada candidato obteve.
hug = 0
zez = 0
lui = 0

print("Digite o voto ou 0 para finalizar")
print("1 - Huguinho")
print("2 - Zezinho")
print("3 - Luizinho")
print("0 - Terminar a votação")

#Inícia um laço infinito
while True:
    voto = int(input("Digite o voto: "))
    if voto == 1: 
        hug = hug + 1
    elif voto == 2:
        zez = zez + 1
    elif voto == 3:
        lui = lui + 1
    else:
        if voto != 0:
            print("Voto inválido, digite 1,2 ou 3")
            
    #Este if simula a condição de saída no final do laço
    if voto == 0: 
        break

    print(f"1 - Huguinho: {hug} votos")
    print(f"2 - Zezinho: {zez} votos")
    print(f"3 - Luizinho: {lui} votos")