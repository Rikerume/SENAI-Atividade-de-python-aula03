def linha():
    print("-------------------------")
linha()
#Questao01: Mostrar a lista composta por numeros inteiros
lista1=[1,2,3,4,5]
print(lista1)

print()
linha()
#Questao2: Mostrar a lista composta por numeros inteiros mas invertido
lista2 = [1,2,3,4,5,6,7,8,9,10]
lista2.reverse()
print(lista2)

print()
linha()
#Questao3: Calcular a media de notas dentro de uma lista
notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)

print()
linha()
#Questao4: Ler um vetor com 20 idades e então mostrar qual a maior idade e a menor
lista4 = [12,23,27,88,49,60]
lista4.sort()

print("Idade:",lista4)
print('A menor idade da lista é {}, e a maior idade é {}'.format(lista4[0], format(lista4[-1])))

print()
linha()
#questao5: deletar itens da lista  
a=0  
while len(lista4) > 0:
    lista4.pop(-1)
    print(lista4)
print("Itens deletados")

print()
linha()
#Questao6: deletar compras do mês
CompraMes = ["arroz", "carne", "feijao"]
ProdutoLimpesa = ["detergentes", "bucha", "alcool"]
ProdutoSorvetes = ["picole", "geladinho"]

CompraMes.extend(ProdutoSorvetes)
CompraMes.extend(ProdutoLimpesa)

resposta = int(input("Deseja excluir alguma lista?\n[1]Sim\n[2]Não\n"))
while resposta == 1:
    resposta = int(input("Deseja excluir alguma lista?\n[1]Sim\n[2]Não\n"))
    if resposta == 1:
        print(CompraMes)
        resposta1 = input("Qual item deseja excluir?")
        if resposta1 in CompraMes:
            CompraMes.remove(resposta1)
        print(CompraMes)
        print("Item excluído")
    else:
        exit()

print()
linha()
#Questao7: Determinar se o numero é par ou impar
def determinar_paridade():
    numero = int(input("Digite o numero: "))
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
print(determinar_paridade())

print()
linha()
#Questao8: Digitar duas palavras e verificar se o reverso de uma delas são a mesma
nome1 = input("Digite o nome: ")
nome2 = input("Digite o nome: ")
rev = ''.join(reversed(nome2))

if nome1 == rev:
    print("As duas palavras são iguais")
else:
    print("As duas palavras não são iguais")


print()
linha()
#Questao9: printar apenas numeros primos
def numeros_primos():
    for i in range(2, 51):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
numeros_primos()
