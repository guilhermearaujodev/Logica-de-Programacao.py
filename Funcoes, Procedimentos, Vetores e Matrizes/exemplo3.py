#Cria um procedimento para exibir na tela o nome do usuário e a saudação de acordo com o horário do dia.
def saudacao2(usuario, hora):
    if hora < 12:
        msg = "Bom dia!"
    elif hora < 18:
        msg = "Boa tarde!"
    else:
        msg = "Boa noite!"
    print("Olá", usuario, ", ", msg ,"Você está logado")

saudacao2("Guilherme", 10)