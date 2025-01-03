# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        
        for l in range(3):
            for c in range(3):
               
                if self._verificar_sequencia(l, c, self.tipo) or self._verificar_sequencia(l, c, Tabuleiro.JOGADOR_0 if self.tipo == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X):
                    return (l, c)

        
        for l in range(3):
            for c in range(3):
                if self._cria_duas_sequencias(l, c):
                    return (l, c)

       
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

     
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            oposto = (2 - canto[0], 2 - canto[1])
            if self.matriz[canto[0]][canto[1]] != Tabuleiro.DESCONHECIDO and self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto

      
        for canto in cantos:
            if self.matriz[canto[0]][canto[1]] == Tabuleiro.DESCONHECIDO:
                return canto

      
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

        return None  

    def _verificar_sequencia(self, l, c, tipo) -> bool:
       
        if self.matriz[l][c] != Tabuleiro.DESCONHECIDO:
            return False

       
        if sum(1 for x in range(3) if self.matriz[l][x] == tipo) == 2:
            return True

        
        if sum(1 for x in range(3) if self.matriz[x][c] == tipo) == 2:
            return True

      
        if l == c and sum(1 for x in range(3) if self.matriz[x][x] == tipo) == 2:
            return True

        
        if l + c == 2 and sum(1 for x in range(3) if self.matriz[x][2 - x] == tipo) == 2:
            return True

        return False

    def _cria_duas_sequencias(self, l, c) -> bool:
       
        if self.matriz[l][c] != Tabuleiro.DESCONHECIDO:
            return False

       
        self.matriz[l][c] = self.tipo
        count = 0

       
        for i in range(3):
            if sum(1 for x in range(3) if self.matriz[i][x] == self.tipo) == 2:
                count += 1
            if sum(1 for x in range(3) if self.matriz[x][i] == self.tipo) == 2:
                count += 1

        if sum(1 for x in range(3) if self.matriz[x][x] == self.tipo) == 2:
            count += 1
        if sum(1 for x in range(3) if self.matriz[x][2 - x] == self.tipo) == 2:
            count += 1

       
        self.matriz[l][c] = Tabuleiro.DESCONHECIDO

        return count >= 2