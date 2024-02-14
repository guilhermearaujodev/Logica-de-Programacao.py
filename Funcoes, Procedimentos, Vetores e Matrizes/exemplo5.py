#Função com Parâmetro
#Criar uma função do tipo booleana que retorne True caso uma nota seja válida ou False se não for.
#No programa principal aplicar a função calculando a média de duas notas.

def nota_valida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False
    
nota1 = float(input("Digite a primeira nota: "))
if (nota_valida(nota1)):
    nota2 = float(input("Digite a segunda nota: "))
    if(nota_valida(nota2)):
        media = (nota1 + nota2) / 2
        print("A media das notas {0} e {1} é {2}".format(nota1,nota2,media))
    else:
        print("A nota 2 => '{0}' é inválida".format(nota2))
else:
    print("A nota 1 => '{0}' é inválida".format(nota1))