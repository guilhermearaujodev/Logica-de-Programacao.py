#CALCULADORA – ESCOLHA
# Dados dois números inteiros e uma operação aritmética desejada calcule a resposta adequada:
# Utilize os símbolos a seguir para ler qual a operação escolhida:
# + soma   -subtração  * multiplicação  / divisão
# esses conjuntos podem conter outros testes de seleção, que por sua vez, também podem conter outros e assim por diante.
#No Python não existe a estrutura "Escolha", mas ela pode ser simulada com o se encadeado (if elif) que utilize apenas a 
#equivalencia (==) como operador.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = str(input("Digite a operação desejada (+ - * /): "))

if operador == '+':
    resultado = numero1 + numero2
    print("Soma = ", resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print("Subtração = ", resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print("Multiplicação = ", resultado)
elif operador == '/':
    if numero2 == 0:
        print("Não existe divisão por zero")
    else:
        resultado = numero1 / numero2
        print("Divisão = ", resultado)
else:
    print("Operador inválido")
