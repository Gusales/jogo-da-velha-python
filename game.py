from random import randint
from tabuleiro import Tabuleiro

class Game():
    def __init__(self, player1, player2):
        self._tabuleiro = Tabuleiro()
        self._player1 = player1
        self._player2 = player2

    def startGame(self):
        x = ""
        o = ""
        if randint(0, 10) % 2 == 0:
            self._player1.setSimbolo("X")
            print(f"{self._player1.getNome()} começa jogando!")
            self._player2.setSimbolo("O")
        else:
            self._player1.setSimbolo("O") 
            self._player2.setSimbolo("X")
            print(f"{self._player2.getNome()} começa jogando!")

            
        rodadas = 1
        while not self._tabuleiro.verificaResultados().get("vencedor"):
            print(f"\nRodada {rodadas}")
            print("Escolha uma das seguintes opções abaixo: \n")
            self._tabuleiro.getTabuleiro()
            opcao = self.escolherOpcao(int(input("Opção: ")))
            if rodadas % 2 != 0:
                self._tabuleiro.verificaPeca(linha=opcao[0], coluna=opcao[1], simbolo="X")
            else:
                self._tabuleiro.verificaPeca(linha=opcao[0], coluna=opcao[1], simbolo="O")
            rodadas += 1

    
    def escolherOpcao(self, opcao):
        opcoes = (
            (0,0),
            (0,1),
            (0,2),
            (1,0),
            (1,1),
            (1,2),
            (2,0),
            (2,1),
            (2,2),
        )

        return opcoes[opcao - 1]
            