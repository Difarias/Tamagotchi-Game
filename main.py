from eventos import Tamagotchi
from sprites import *
import os
from pathlib import Path

"""
Desenvolvedores: Gabriela Zerbone Magno Baptista e Diêgo Farias de Freitas

Última modificação: 18/07
"""

def titulos(x):
    if x == 1:
        print("\n")

        print("█████████       ▒▒▒▒▒▒▒       ▄████▄\n█▄█████▄█       ▒─▄▒─▄▒       ███▄█▀\n█▼▼▼▼▼          ▒▒▒▒▒▒▒       ████            \n█████████       ▒▒▒▒▒▒▒       █████▄\n ██ ██          ▒ ▒ ▒ ▒       ▀████▀\n FEBRIX       FANTASMINHA     PACMAN\n   (1)            (2)          (3)")

    else:
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝")
        
'''
Essa função retornará a quantidade de caracteres escrito dentro de um arquivo, se for zero
o arquivo estará sem nenhuma informação salva; diferente disso, algo estará salvo ali dentro.
'''
def ler_arquivo():
    arquivo = (os.stat("bancoDados.dat").st_size) #retorna o tamanho do arquivo, se for zero, arquivo vazio
    return int(arquivo)

'''
Essa função tem por objetivo armazenar o personagem que o usuário escolheu na primeira iteração,
lendo o primeiro caractere do arquivo(onde salvamos tal escolha dele), ou seja, posição [0].
'''
def armazenar_personagem():
    arquivo = arquivo = open("bancoDados.dat", "r")
    conteudo = arquivo.read() #armazena na variavel conteudo tudo que tem dentro do arquivo
    op_personagem = conteudo.split('@') #o split identificará no conteúdo cada aparecimento do @(nosso separador de informações) e retornará uma lista. Ex: ['personagem', 'nome', 'level', 'xp']
    return int(op_personagem[0])

print('-'*50)
print('INICIAR JOGO')
print('-'*50)

tamanhoArquivo = ler_arquivo()
titulos(0)

if (tamanhoArquivo == 0): #iniciará o jogo do zero, perguntando o personagem inicial e seu nome
    titulos(1)
    personagem = int(input('Escolha seu personagem -->'))
    if personagem >= 1 and personagem <= 3:
        nome = input('Digite o nome do seu pet: ')
        pet = Tamagotchi(nome, personagem)
    else:
        exit("Esse personagem não existe, tente novamente")
else:
    opcao = armazenar_personagem()
    pet = Tamagotchi(personagem=opcao) #"resgata" o personagem escolhido antes, passa-se como parâmetro para permanecer com ele 
    pet.setterDados() 

os.system("cls") #limpa a tela

#MENU DE AÇÕES-INTERAÇÃO COM O USUÁRIO
op = None
pet.imprimirDados()
while op != 0:

    print('1-Alimentar')
    print('2-Brincar')
    print('3-Curar')
    print('4-Tomar banho')
    print('5-Dormir')
    print('0-Sair')
    op = int(input('Digite o número da ação desejada --> '))

    if op >= 1 and op <= 5:
        pet.virtual_pet.imprimeAcao() #Na classe Tamagotchi, fizemos composição de classes, então acessamos diretamente a função da classe composta pela variável virtual_pet
        pet.eventos(op)
    else:
        pet.salvarDados() #antes de sair do jogo, salva-se os dados!
        exit('Você saiu do jogo...')
