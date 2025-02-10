import random

lampada_casa = []


def f(acesas):
    return 1


# 1
class Estado:
    def __init__(self, acesas):
        self.acesas = acesas
        self.f = f(acesas)


# 2
def estado_inicial():
    acesas = []
    for _ in lampada_casa:
        acesas.append(random.choice([0, 1]))

    return Estado(acesas)


# 4
def mutacao(estado):
    acesas = estado.acesas.copy()
    i = random.randint(0, len(lampada_casa) - 1)
    acesas[i] = 1 - acesas[i]

    return Estado(acesas)


# 5
def cruzamento(pai1, pai2):
    acesas = []
    for a1, a2 in zip(pai1.acesas, pai2.acesas):
        acesas.append(random.choice([a1, a2]))

    return Estado(acesas)
