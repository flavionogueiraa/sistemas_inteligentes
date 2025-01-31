import math
import random


# Função objetivo
def f(x):
    return (1 / (x * x + 1)) * math.cos(10 * x)


class Estado:
    def __init__(self, x):
        self.x = x
        self.f = f(x)


def exibe(estado):
    print(f"x = {estado.x}, f = {estado.f}")


def estado_inicial():
    return Estado(random.uniform(-10, 10))


def melhor_sucessor(estado):
    melhor = estado
    atual = estado
    for _ in range(100):
        deltax = random.uniform(-1, 1)
        vizinho = Estado(atual.x + deltax)
        if vizinho.f > melhor.f:
            melhor = vizinho
    return melhor


def prob(deltaE, T):
    return math.exp(deltaE / T)


T = 1000
temp_crit = 0.0001
taxa_resfriamento = 0.999
atual = estado_inicial()

while T > temp_crit:
    T = taxa_resfriamento * T
    vizinho = melhor_sucessor(atual)
    deltaE = vizinho.f - atual.f
    if deltaE > 0 or random.uniform(0, 1) < prob(deltaE, T):
        atual = vizinho
        exibe(atual)

print("Solução final:")
exibe(atual)
