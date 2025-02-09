import random

tempos = []
qtd_distritos = 10
qtd_centros = 2


def f(distritos_escolhidos):
    return 1


# 1
class Estado:
    def __init__(self, distritos_escolhidos):
        self.distritos_escolhidos = distritos_escolhidos
        self.f = f(distritos_escolhidos)


# 2
def estado_inicial():
    distritos_escolhidos = []
    for _ in range(qtd_distritos):
        distritos_escolhidos.append(random.choice([0, 1]))

    return Estado(distritos_escolhidos)


# 4
def mutacao(estado):
    distritos_escolhidos = estado.distritos_escolhidos.copy()
    i = random.randint(0, len(distritos_escolhidos) - 1)
    distritos_escolhidos[i] = 1 - distritos_escolhidos[i]

    return Estado(distritos_escolhidos)


# 5
def cruzamento(pai1, pai2):
    distritos_escolhidos = []
    for d1, d2 in zip(pai1.distritos_escolhidos, pai2.distritos_escolhidos):
        distritos_escolhidos.append(random.choice([d1, d2]))

    return Estado(distritos_escolhidos)
