class Estado:
    def __init__(self, valor, pai):
        self.valor = valor
        self.pai = pai


def exibe(estado):
    print(estado.valor)


def estado_inicial():
    return Estado(0, None)


def objetivo(estado):
    return estado.valor == 6


def expande(estado):
    valor = estado.valor
    return [Estado(2 * valor + 1, estado), Estado(2 * valor + 2, estado)]


lista = []


def enfileira(estado):
    lista.append(estado)


def vazia():
    return lista == []


def desenfileira():
    return lista.pop(0)


def mostrar_caminho(estado):
    if estado is None:
        return

    mostrar_caminho(estado.pai)
    exibe(estado)


enfileira(estado_inicial())
while not vazia():
    atual = desenfileira()
    exibe(atual)
    if objetivo(atual):
        print("Solução encontrada!")
        mostrar_caminho(atual)
        break

    filhos = expande(atual)
    for filho in filhos:
        enfileira(filho)
