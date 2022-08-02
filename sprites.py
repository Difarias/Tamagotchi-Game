from abc import ABC, abstractmethod
import os
'''
Utiliza-se o conceito de interface em prol da construção das classes derivadas, servindo de modelo para as mesmas.

A classe Sprites molda a construção das demais classes, as quais são responsáveis por imprimir os personagens do jogo.
'''
class Sprites(ABC):

    @abstractmethod
    def imprimeTitulo(self)->None:
        pass

    @abstractmethod
    def sprite_alimentar(self)->None:
        pass

    @abstractmethod
    def sprite_brincar(self)->None:
        pass

    @abstractmethod
    def sprite_curar(self)->None:
        pass

    @abstractmethod
    def sprite_banhar(self)->None:
        pass

    @abstractmethod
    def sprite_dormir(self)->None:
        pass

    @abstractmethod
    def imprimeAcao(self)->None:
        pass

class Febrix(Sprites):

    def imprimeTitulo(self)->None:
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝\n")

    def sprite_alimentar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print("█████████\n█▄█████▄█\n█▼▼▼▼▼\n█  ██\n█▲▲▲▲▲\n█████████\n ██ ██\n")

    def sprite_brincar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print("█████████  ╔═══╗♪\n█▄█████▄█  ║███║ ♫\n█▼▼▼▼▼     ║(●)║♫\n█████████  ╚═══╝ ♪\n ██ ██")

    def sprite_curar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print("█████████    ┌─┐\n█▄█████▄█  ┌─┘ └─┐\n█▼▼▼▼▼     └─┐ ┌─┘\n█████████    └─┘\n ██ ██ \n ")

    def sprite_banhar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('┌┐       ┌┐\n││       ││\n│└─┬──┬─┐│└─┬──┐\n│┌┐│┌┐│┌┐┤┌┐│┌┐│\n│└┘│┌┐│││││││└┘│ ┌┐┌┐┌┐\n└──┴┘└┴┘└┴┘└┴──┘ └┘└┘└┘\n█████████\n█▄█████▄█\n█▼▼▼▼▼\n█████████\n ██ ██\n')

    def sprite_dormir(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print("█████████\n█─█████─█   ZzzZzzz\n█████████\n█████████\n ██ ██")

    def imprimeAcao(self, acao=0)->None:
        if acao == 1:
            self.sprite_alimentar()
        elif acao == 2:
            self.sprite_brincar()
        elif acao == 3:
            self.sprite_curar()
        elif acao == 4:
            self.sprite_banhar()
        else:
            self.sprite_dormir()

class Fantasminha(Sprites):
    def imprimeTitulo(self)->None:
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝\n")

    def sprite_alimentar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▄▒▒▒  ▒\n▒ ▒ ▒ ▒')

    def sprite_brincar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print(
            '▒▒▒▒▒▒▒╔═══╗♪\n▒─▄▒─▄▒║███║ ♫\n▒▒▒▒▒▒▒║ (●)  ║♫\n▒▒▒▒▒▒▒╚═══╝ ♪\n▒ ▒ ▒ ▒')

    def sprite_curar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▒▒▒▒▒▒▒    ┌─┐\n▒─▄▒─▄▒  ┌─┘ └─┐\n▒▒▒▒▒▒▒  └─┐ ┌─┘\n▒▒▒▒▒▒▒    └─┘\n▒ ▒ ▒ ▒')

    def sprite_banhar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('┌┐       ┌┐\n││       ││\n│└─┬──┬─┐│└─┬──┐\n│┌┐│┌┐│┌┐┤┌┐│┌┐│\n│└┘│┌┐│││││││└┘│ ┌┐┌┐┌┐\n└──┴┘└┴┘└┴┘└┴──┘ └┘└┘└┘\n▒▒▒▒▒▒▒\n▒─▄▒─▄▒\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒ ▒ ▒ ▒')

    def sprite_dormir(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▒▒▒▒▒▒▒\n▒─ ▒─ ▒   ZzzzZzzz\n▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒\n▒  ▒  ▒')

    def imprimeAcao(self, acao=0)->None:
        if acao == 1:
            self.sprite_alimentar()
        elif acao == 2:
            self.sprite_brincar()
        elif acao == 3:
            self.sprite_curar()
        elif acao == 4:
            self.sprite_banhar()
        else:
            self.sprite_dormir()

class Pacman(Sprites):
    def imprimeTitulo(self)->None:
        print("██╗   ██╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗\n██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║\n██║   ██║█████╗  ███████╗██║     ██║  ███╗██║   ██║   ██║   ██║     ███████║██║\n██║   ██║██╔══╝  ╚════██║██║     ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║\n╚██████╔╝███████╗███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║\n ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝\n")

    def sprite_alimentar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▄████▄\n███▄█▀\n████     █     █\n█████▄\n ▀████▀')

    def sprite_brincar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▄████▄  ╔═══╗♪\n███▄█▀  ║███║ ♫\n████        ║  (●)  ║♫\n█████▄  ╚═══╝ ♪\n ▀████▀')

    def sprite_curar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▄████▄    ┌─┐\n███▄█▀  ┌─┘ └─┐\n████    └─┐ ┌─┘\n█████▄    └─┘\n ▀████▀')

    def sprite_banhar(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('┌┐       ┌┐\n││       ││\n│└─┬──┬─┐│└─┬──┐\n│┌┐│┌┐│┌┐┤┌┐│┌┐│\n│└┘│┌┐│││││││└┘│┌┐┌┐┌┐\n└──┴┘└┴┘└┴┘└┴──┘└┘└┘└┘\n▄████▄\n███▄█▀\n████    \n█████▄\n ▀████▀')

    def sprite_dormir(self)->None:
        os.system("cls")
        self.imprimeTitulo()
        print('▄████▄\n███─█▀    ZzzzZzzz\n████\n█████▄\n ▀████▀\n')

    def imprimeAcao(self, acao=0)->None:
        if acao == 1:
            self.sprite_alimentar()
        elif acao == 2:
            self.sprite_brincar()
        elif acao == 3:
            self.sprite_curar()
        elif acao == 4:
            self.sprite_banhar()
        else:
            self.sprite_dormir()
