#DESVIO ENCADEADO 

# Dado o salário do funcionário, calcular o imposto de renda e o salário líquido de acordo com os seguintes critérios:
# 1- Salário até 1900 insento - 0%
# 2- Salário entre 1900.01 e 2800 - 15%
# 3- Salário acima de 2800.01 - 27,5%
sal = float(input("Digite o seu salário: "))

if sal <= 1900: 
    imposto_renda = 0
elif sal <= 2800:
    imposto_renda = sal * 0.15
else: 
    imposto_renda = sal * 0.275

sal_liquido = sal - imposto_renda

# 2.f vai interpretar que são duas casas decimais. 
print(f"Imposto de Renda: {imposto_renda:.2f}")
print(f"Salário Líquido: {sal_liquido:.2f}")