from player import Player
from game import Game

player1 = Player()
player2 = Player()

def welcome():
    print("\nBem vindos ao \033[1;30mJogo da Velha!\033[m")
    print("Vamos começar com os nomes dos jogadores: ")
    player1.setNome()
    player2.setNome()

    print(f"Que bom poder jogar com vocês {player1.getNome()} e {player2.getNome()}")

def menu():
    print("Escolha uma opção: ")
    print("1 - Começar o Jogo")
    print("2 - Ver quantidade de pontos")
    print("3 - Sair do jogo")

    option = 0                                                                                                                      
    while option != 3:
        option = int(input("\nOpção: "))

        match option:
            case 1:
                # Começar o jogo;
                startGame()
                return
            case 2:
                # mostrar o placar
                return
            case 3:
                print("Muito obrigado por ter jogado conosco!\nPlacar no final:")
                print("Até a próxima!")
                exit()


def startGame():
    game = Game(player1, player2)
    game.startGame()

def main():
    welcome()
    menu()

main()