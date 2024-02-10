# Exemplo 1 - Desvio Simples
# Dada uma venda, calcular e exibir o desconto de 10% caso a venda seja acima de 300 reais.
venda = float(input("Digite a venda: "))
if venda > 300:
    desconto = venda * 10 / 100
    venda = venda - desconto
print("Novo valor: ", venda)