class Estado:
    def __init__(self, pedras, pai):
        self.pedras = pedras
        self.pai = pai


def estado_inicial():
    return Estado([1, 2, 3, None, 4, 5, 6], None)


def exibe(estado):
    print(estado.pedras)


def objetivo(estado):
    return estado.pedras == [4, 5, 6, None, 1, 2, 3]


def pular(estado, sapo):
    index_sapo = estado.pedras.index(sapo)
    origem, destino = None, None

    if sapo <= 3:
        try:
            if (
                estado.pedras[index_sapo + 2] is None
                and estado.pedras[index_sapo + 1] > 3
            ):
                origem, destino = index_sapo, index_sapo + 2
        except IndexError:
            pass

        try:
            if estado.pedras[index_sapo + 1] is None:
                origem, destino = index_sapo, index_sapo + 1
        except IndexError:
            pass

    else:
        try:
            if (
                estado.pedras[index_sapo - 2] is None
                and estado.pedras[index_sapo - 1] <= 3
            ):
                origem, destino = index_sapo, index_sapo - 2
        except IndexError:
            pass

        try:
            if estado.pedras[index_sapo - 1] is None:
                origem, destino = index_sapo, index_sapo - 1
        except IndexError:
            pass

    if origem is None or destino is None:
        return None

    pedras = estado.pedras.copy()
    pedras[destino] = pedras[origem]
    pedras[origem] = None

    return Estado(pedras, estado)


def pular_sapo1(estado):
    return pular(estado, 1)


def pular_sapo2(estado):
    return pular(estado, 2)


def pular_sapo3(estado):
    return pular(estado, 3)


def pular_sapo4(estado):
    return pular(estado, 4)


def pular_sapo5(estado):
    return pular(estado, 5)


def pular_sapo6(estado):
    return pular(estado, 6)


def expande(estado):
    acoes = [
        pular_sapo1,
        pular_sapo2,
        pular_sapo3,
        pular_sapo4,
        pular_sapo5,
        pular_sapo6,
    ]
    estados_filhos = []
    for acao in acoes:
        f = acao(estado)
        if f is not None:
            estados_filhos.append(f)

    return estados_filhos


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
    if objetivo(atual):
        mostrar_caminho(atual)
        break

    filhos = expande(atual)
    for filho in filhos:
        enfileira(filho)
