import math
import os
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

    for _ in range(5):
        deltax = random.uniform(-1, 1)
        vizinho = Estado(estado.x + deltax)
        if vizinho.f > melhor.f:
            melhor = vizinho

    return vizinho


def prob(deltaE, T):
    return math.exp(deltaE / T)


T = 1000
T_crit = 0.0001
taxa_resfriamento = 0.999
atual = estado_inicial()

while T > T_crit:
    T = T * taxa_resfriamento
    vizinho = melhor_sucessor(atual)
    deltaE = vizinho.f - atual.f

    if deltaE > 0 or prob(deltaE, T) > random.uniform(0, 1):
        atual = vizinho
        exibe(atual)

print("Solução final")
exibe(atual)
