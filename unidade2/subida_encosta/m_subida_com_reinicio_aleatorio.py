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
    for _ in range(5):
        deltax = random.uniform(-0.01, 0.01)
        vizinho = Estado(atual.x + deltax)
        if vizinho.f > melhor.f:
            melhor = vizinho
    return melhor


melhor = estado_inicial()

while True:
    atual = estado_inicial()
    while True:
        vizinho = melhor_sucessor(atual)
        if vizinho.f <= atual.f:
            break
        atual = vizinho

    if atual.f > melhor.f:
        exibe(atual)
        melhor = atual
