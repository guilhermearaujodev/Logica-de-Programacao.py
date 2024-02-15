"""
LISTAS EM PYTHON
- O conteúdo dos elementos é heterogêneo
- Os elementos são dinâmicos, ou seja, acrescentamos ou excluimos quando quisermos
- O append acrescenta um item no final. lista.append(45)
- O insert permite editar um elemento. list.insert(indice,conteudo)
- O pop remove o ultimo elemtno da lista. lista.pop()
- O clear apaga todos os elemtnos da lista. lista.clear
""" 
## Listas em python pode ter elemtnos heterogeneos 
#         0   1    2     3
lista = ["a", 2, True, 4.5]
print(lista)

## Adicionando um elemento no final da lista
lista.append (45)
print(lista)

## Editando um elemento existente
lista.insert(0,"TESTE")
print(lista)

## O pop remove o último elemento
lista.pop()
print(lista)

## Apaga todos os elementos 
lista.clear()
print(lista)

## Preenchendo 5 elementos na lista
lista = []
for cont in range(0, 5, 1):
    x = float(input("Digite um elemento: "))
    lista.append(x)
print(lista)

## Exibindo os 5 elementos da lista - FORMA 1
for i in range(0,5,1):
    print(lista[1])

## Exibindo os 5 elementos da lista - FORMA 2
for elem in lista:
    print(elem)



## MANIPULANDO MATRIZ - PYTHON 

matriz = [ [0,0], [0,0],[0,0],[0,0] ]

# 1 - PREENCHER A MATRIZ
print("Preenchendo a matriz...")
for l in range(4):
    for c in range(2):
        matriz [l][c] = int(input(f"Matriz[{l}][{c}]= "))

# 2 - EXIBIR A MATRIZ
print("\nExibindo a matriz...")
for l in range(4):
    for c in range(2):
        print(f"{matriz[l][c]}\t", end = "")
    print()