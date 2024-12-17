# -*- coding: utf-8 -*-
from random import randint
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):

        jogada = self.regra_1(Tabuleiro.JOGADOR_X)  
        if jogada:
            return jogada
        jogada = self.regra_1(Tabuleiro.JOGADOR_0)  
        if jogada:
            return jogada

        jogada = self.regra_2()
        if jogada:
            return jogada

        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        jogada = self.regra_4()
        if jogada:
            return jogada

        jogada = self.regra_5()
        if jogada:
            return jogada

        return self.regra_6()

    def regra_1(self, jogador):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    if self.verifica_sequencia(l, c, jogador):
                        return (l, c)
        return None

    def verifica_sequencia(self, l, c, jogador):
        if self.matriz[l][(c + 1) % 3] == jogador and self.matriz[l][(c + 2) % 3] == jogador:
            return True
        if self.matriz[(l + 1) % 3][c] == jogador and self.matriz[(l + 2) % 3][c] == jogador:
            return True
        if l == c and self.matriz[(l + 1) % 3][(c + 1) % 3] == jogador and self.matriz[(l + 2) % 3][(c + 2) % 3] == jogador:
            return True
        return False

    def regra_2(self):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    if self.cria_duas_sequencias(l, c):
                        return (l, c)
        return None

    def cria_duas_sequencias(self, l, c):
        return False  

    def regra_4(self):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opostos = [(2, 2), (2, 0), (0, 2), (0, 0)]
        for i, (l, c) in enumerate(cantos):
            if self.matriz[l][c] == Tabuleiro.JOGADOR_0 and self.matriz[opostos[i][0]][opostos[i][1]] == Tabuleiro.DESCONHECIDO:
                return opostos[i]
        return None

    def regra_5(self):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (l, c) in cantos:
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        return None

    def regra_6(self):
        
        lista = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
        return lista[randint(0, len(lista)-1)]