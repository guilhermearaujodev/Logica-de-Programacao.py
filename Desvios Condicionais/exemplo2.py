# Exemplo 2 - DESVIO COMPOSTO
# Uma empresa dará aumento para os seus funcionários.
# Caso ele trabalhe menos de três anos na empresa, ganhará 5% de aumento, caso contrário 10%.
tempo_empresa = int(input("Digite o seu tempo de casa: "))
sal = float(input("Digite o seu salário: "))

if tempo_empresa < 3:
    aumento = sal * 0.05
else:
    aumento = sal * 0.1

novo_sal = sal + aumento
print("O seu salário foi de", sal, " para", novo_sal)
