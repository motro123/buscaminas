class celda():


    posibles = "ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&"

    def __init__(self, n1, n2, bomba):
        self.n1 = n1
        self.n2 = n2
        self.bomba = bomba
        self.adyacentes = [None] *6
        self.bomba = bomba
        self.abierta = False
        self.marca = False
        self.duda = False
        self.nady = 0
        # if self.n2 + 1 % 2 == 0:
        #
        #     self.adyacentes.insert(0, celda(matriz[self.buscarCerca(self.n1, -1)][self.n2]))
        #     self.adyacentes.insert(1, celda(matriz[self.buscarCerca(self.n1, -1)][self.buscarCerca(self.n2, +1)]))
        #     self.adyacentes.insert(2, celda(matriz[self.n1][self.buscarCerca(self.n2, +1)]))
        #     self.adyacentes.insert(3, celda(matriz[self.n1][self.buscarCerca(self.n2, -1)]))
        #     self.adyacentes.insert(4, celda(matriz[self.buscarCerca(self.n1, +1)][self.n2]))
        #     self.adyacentes.insert(5, celda(matriz[self.buscarCerca(self.n1, +1)][self.buscarCerca(self.n2, +1)]))
        #     for i in self.adyacentes:
        #         if celda(i).bomba:
        #             self.nady = self.nady + 1
        #
        # elif self.n2 + 1 % 2 != 0:
        #     self.adyacentes.insert(matriz[self.buscarCerca(self.n1, -1)][self.n2])
        #     self.adyacentes.insert(matriz[self.buscarCerca(self.n1, -1)][self.buscarCerca(self.n2, -1)])
        #     self.adyacentes.insert(matriz[self.n1][self.buscarCerca(self.n2, +1)])
        #     self.adyacentes.insert(matriz[self.n1][self.buscarCerca(self.n2, -1)])
        #     self.adyacentes.insert(matriz[self.buscarCerca(self.n1, +1)][self.n2])
        #     self.adyacentes.insert(matriz[self.buscarCerca(self.n1, +1)][self.buscarCerca(self.n2, -1)])
        #     for i in self.adyacentes:
        #         if celda(i).bomba:
        #             self.nady = self.nady + 1

    # def cuantosAdyacentes(self, matriz):
    #
    #     if  self.n2+1 % 2 == 0:
    #
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1,-1)][self.n2])
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, -1)][self.buscarCerca(self.n2, +1)])
    #         self.adyacentes.insert(matriz[self.n1][self.buscarCerca(self.n2, +1)])
    #         self.adyacentes.insert(matriz[self.n1][self.buscarCerca(self.n2, -1)])
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, +1)][self.n2])
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, +1)][self.buscarCerca(self.n2, +1)])
    #     elif self.n2+1 %2 != 0:
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, -1)][self.n2])
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, -1)][self.buscarCerca(self.n2, -1)])
    #         self.adyacentes.insert(matriz[self.n1][self.buscarCerca(self.n2, +1)])
    #         self.adyacentes.insert(matriz[self.n1][self.buscarCerca(self.n2, -1)])
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, +1)][self.n2])
    #         self.adyacentes.insert(matriz[self.buscarCerca(self.n1, +1)][self.buscarCerca(self.n2, -1)])
    #
    #         for obj in self.adyacentes:
    #
    #             if isinstance(obj,celda):

    def buscarCerca(self, letra, incdec):
        lista = list(self.posibles)
        ret = 0

        for x in range(0, 29):
            if x.__eq__(letra):
                ret = lista[x + incdec]

        return ret
