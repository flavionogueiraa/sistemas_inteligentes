import random


def f(colunas):
    return 1


# 1
class Estado:
    def __init__(self, colunas):
        self.colunas = colunas
        self.f = f(colunas)


# 2
def estado_inicial():
    colunas = []
    for _ in range(8):
        colunas.append(random.randint(0, 7))

    return Estado(colunas)


# 4
def mutacao(estado):
    colunas = estado.colunas.copy()
    i = random.randint(0, 7)
    colunas[i] = random.randint(0, 7)

    return Estado(colunas)


# 5
def cruzamento(pai1, pai2):
    colunas = []
    for c1, c2 in zip(pai1.colunas, pai2.colunas):
        colunas.append(random.choice([c1, c2]))

    return Estado(colunas)
