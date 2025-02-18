class Tabuleiro():
    _tabuleiro = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    _vencedor = False
    
    def getTabuleiro(self):
        for i, linha in enumerate(self._tabuleiro):
            print(" | ".join(map(str, linha)))
            if i < len(self._tabuleiro) - 1:
                print("-" * 9)
        return self._tabuleiro

    def _setPeca(self, linha, coluna, simbolo):
        self._tabuleiro[linha][coluna] = simbolo
    
    def verificaPeca(self, linha, coluna, simbolo):
        celula = self._tabuleiro[linha][coluna]
        
        if celula == "X" or celula == "O":
            print("Aqui já foi marcado!")
        else:
            self._setPeca(linha, coluna, simbolo)
    
    def _pegaDiagonais(self):
        tamanhoMinMax = range(0,3)

        diagonalPrincipal = []
        diagonalSecundaria = []

        for linha in tamanhoMinMax:
            for coluna in tamanhoMinMax:
                if(linha == coluna):
                    diagonalPrincipal.append(self._tabuleiro[linha][coluna])

        aux = 2
        for l in range(0,3):
            for c in range(2,-1,-1):
                if c == aux:
                    diagonalSecundaria.append(self._tabuleiro[l][c])
            aux -= 1

        return [diagonalPrincipal, diagonalSecundaria]
    
    def _transformaColunaEmLinha(self):
        tabuleiroInvertido = [[0,0,0], [0,0,0], [0,0,0]]

        for linha in range(0, 3):
            for coluna in range(0, 3):
                tabuleiroInvertido[linha][coluna] = self._tabuleiro[coluna][linha]

        return tabuleiroInvertido
    
    def _verificaLinha(self, linha):
        x = 0
        o = 0
        for item in linha:
            if item == 'X':
                x+=1
            elif item == 'O':
                o+=1
        
        return { "x": x, "o": o, "tem_vencedor": x == 3 or o == 3 }
    
    def verificaResultados(self):
        diagonais = self._pegaDiagonais()

        for linha in self._tabuleiro:
            if self._verificaGanhador(linha).get("vencedor") != False:
                self._vencedor = self._verificaGanhador(linha).get("vencedor")

        for linha in diagonais:
            if self._verificaGanhador(linha).get("vencedor") != False:
                self._vencedor = self._verificaGanhador(linha).get("vencedor")

        for linha in self._transformaColunaEmLinha():
            if self._verificaGanhador(linha).get("vencedor") != False:
                self._vencedor = self._verificaGanhador(linha).get("vencedor")

        return { "vencedor": self._vencedor }

    def _verificaGanhador(self, linha):
        tem_vencedor = self._verificaLinha(linha).get("tem_vencedor")
        if tem_vencedor:
            x = self._verificaLinha(linha).get("x")
            o = self._verificaLinha(linha).get("o")
            return { "vencedor": "x" if x > o else "o" }
        else:
            return { "vencedor": False }