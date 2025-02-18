from utils import printNameWithColor

class Player():
    _nome = ""
    _simbolo = ""
    def __init__(self):
        self._pontos = 0

    def setNome(self) -> str:
        name = str(input("Digite seu nome: "))
        if name.lower() == "emilly" or name.lower() == "emy":
            self._nome = printNameWithColor("purple", name)
        elif name.lower() == "gustavo" or name.lower() == "gu":
            self._nome = printNameWithColor("blue", name)
        else:
            self._nome = name


    def getNome(self) -> str:
        return self._nome
    
    def setSimbolo(self, simbolo):
        self._simbolo = simbolo
        print(f"{self._nome} você ficou com {simbolo}")

    def getSimbolo(self):
        return self._simbolo

    def pontuou(self):
        self._pontos += 1
    
    def getPontos(self):
        return self._pontos