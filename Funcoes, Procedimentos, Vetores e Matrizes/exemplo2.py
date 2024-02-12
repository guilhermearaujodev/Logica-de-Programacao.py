#Saudações com parâmetros de acordo com o horário do dia.
#subalgoritmos 
def saudacao(hora):
    if hora < 12:
        msg = "Bom dia,"
    elif hora < 18:
        msg = "Boa tarde,"
    else:  
        msg = "Boa noite,"
    print(msg, "Seja bem vindo!")

#programa principal
saudacao(20)