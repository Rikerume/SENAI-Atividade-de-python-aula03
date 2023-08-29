#Questao1

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

minha_bola = Bola("vermelho", 10, "couro")

print(minha_bola.mostraCor()) 


minha_bola.trocaCor("azul")


print(minha_bola.mostraCor())

#Questao2
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado ** 2

meu_quadrado = Quadrado(5)


print(meu_quadrado.retornarLado()) 

meu_quadrado.mudarLado(7)


print(meu_quadrado.retornarLado())


area = meu_quadrado.calcularArea()
print(area) 

#Questao3
class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

meu_retangulo = Retangulo(0, 0)


lado_a = float(input("Informe a medida do lado A do local: "))
lado_b = float(input("Informe a medida do lado B do local: "))

meu_retangulo.mudarLados(lado_a, lado_b)


area = meu_retangulo.calcularArea()
perimetro = meu_retangulo.calcularPerimetro()


area_do_piso = float(input("Informe a área de um piso: "))
comprimento_rodape = float(input("Informe o comprimento de um rodapé: "))


quantidade_pisos = area / area_do_piso
quantidade_rodapes = perimetro / comprimento_rodape


print("Quantidade de pisos necessários:", quantidade_pisos)
print("Quantidade de rodapés necessários:", quantidade_rodapes)

#Questao4

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

pessoa = Pessoa("João", 18, 70, 170)

print(pessoa.nome)   
print(pessoa.idade) 
print(pessoa.peso)  
print(pessoa.altura) 

pessoa.envelhecer()

print(pessoa.idade) 
print(pessoa.altura) 

pessoa.engordar(5)
pessoa.emagrecer(3)

print(pessoa.peso)  

#Questao5
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibirSaldo(self):
        print("Saldo atual:", self.saldo)

conta = ContaCorrente("1234", "João")

print(conta.numero_conta)     
print(conta.nome_correntista)    
print(conta.saldo)           

conta.alterarNome("Maria")

conta.deposito(100)

conta.saque(50)

conta.exibirSaldo()   

#Questao6

class TV:
    def __init__(self, canal_inicial=1, volume_inicial=50):
        self.canal = canal_inicial
        self.volume = volume_inicial

    def alterarCanal(self, novo_canal):
        if novo_canal >= 1 and novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido. O canal deve estar entre 1 e 100.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo alcançado.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo alcançado.")

    def exibirStatus(self):
        print("Canal:", self.canal)
        print("Volume:", self.volume)

tv = TV()

tv.exibirStatus()  
tv.alterarCanal(5)
tv.aumentarVolume()
tv.exibirStatus() 
tv.diminuirVolume()
tv.exibirStatus()

#Questao7

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, valor):
        self.fome = valor

    def alterarSaude(self, valor):
        self.saude = valor

    def alterarIdade(self, valor):
        self.idade = valor

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        return self.fome + self.saude

meu_bichinho = BichinhoVirtual("Bob")


meu_bichinho.alterarNome("Charlie")


meu_bichinho.alterarFome(50)
meu_bichinho.alterarSaude(80)
meu_bichinho.alterarIdade(2)


print(meu_bichinho.retornarNome())   
print(meu_bichinho.retornarFome())    
print(meu_bichinho.retornarSaude())   
print(meu_bichinho.retornarIdade())   
print(meu_bichinho.retornarHumor())   

#Questao8

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if len(self.bucho) == 0:
            print("O bucho está vazio.")
        else:
            print("Conteúdo do bucho:", ", ".join(self.bucho))

    def digerir(self):
        if len(self.bucho) == 0:
            print("O macaco não comeu nada.")
        else:
            print("Digerindo...")
            self.bucho = []
            print("O bucho está vazio agora.")

macaco1 = Macaco("Barbie")
macaco2 = Macaco("Ken")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")


macaco2.comer("Uva")
macaco2.comer("Pêssego")
macaco2.comer("Morango")


macaco1.verBucho() 

macaco2.verBucho()  

macaco1.digerir()  

macaco2.digerir()   

macaco1.verBucho()   

macaco2.verBucho()

#Questao9
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("Coordenadas do ponto: ({}, {})".format(self.x, self.y))


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def imprimirCentro(retangulo):
    centro = retangulo.encontrarCentro()
    print("Centro do retângulo:")
    centro.imprimir()


def alterarRetangulo(retangulo):
    print("1. Alterar ponto inicial")
    print("2. Alterar largura")
    print("3. Alterar altura")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        novo_x = int(input("Digite o novo valor de x: "))
        novo_y = int(input("Digite o novo valor de y: "))
        novo_ponto_inicial = Ponto(novo_x, novo_y)
        retangulo.ponto_inicial = novo_ponto_inicial
    elif opcao == 2:
        nova_largura = int(input("Digite a nova largura: "))
        retangulo.largura = nova_largura
    elif opcao == 3:
        nova_altura = int(input("Digite a nova altura: "))
        retangulo.altura = nova_altura
    else:
        print("Opção inválida.")



retangulo1 = Retangulo(Ponto(0, 0), 5, 3)
retangulo2 = Retangulo(Ponto(2, 2), 4, 6)

while True:
    print("\n=== MENU ===")
    print("1. Imprimir centro do retângulo")
    print("2. Alterar retângulo")
    print("3. Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    if opcao_menu == 1:
        imprimirCentro(retangulo1)
        imprimirCentro(retangulo2)
    elif opcao_menu == 2:
        print("Qual retângulo deseja alterar?")
        print("1. Retângulo 1")
        print("2. Retângulo 2")
        opcao_retangulo = int(input("Escolha uma opção: "))

        if opcao_retangulo == 1:
            alterarRetangulo(retangulo1)
        elif opcao_retangulo == 2:
            alterarRetangulo(retangulo2)
        else:
            print("Opção inválida.")
    elif opcao_menu == 3:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")

#Questao10

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            print("Abastecimento realizado.")
            print("Quantidade de litros abastecidos:", litros_abastecidos)
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print("Abastecimento realizado.")
            print("Valor a pagar:", valor_pagar)
        else:
            print("Não há combustível suficiente na bomba.")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

bomba = BombaCombustivel("Gasolina", 5.0, 1000)


bomba.abastecerPorValor(50)  


bomba.abastecerPorLitro(20)

bomba.alterarValor(4.5)

bomba.alterarCombustivel("Etanol")


bomba.alterarQuantidadeCombustivel(800)
