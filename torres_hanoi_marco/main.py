class Estado:
    def __init__(self, torres, pai):
        self.torres = torres
        self.pai = pai


def exibe(estado):
    for torre in estado.torres:
        print(torre)
    print("-----------")


def estado_inicial():
    return Estado([[3, 2, 1], [], []], None)


def objetivo(estado):
    return estado.torres[2] == [3, 2, 1]


def torre_valida(torre):
    if len(torre) <= 1:
        return True

    for i in range(1, len(torre)):
        if torre[i] > torre[i - 1]:
            return False

    return True


def valido(estado):
    for torre in estado.torres:
        if not torre_valida(torre):
            return False

    return True


def transfere(estado, origem, destino):
    if estado.torres[origem] == []:
        return None

    torres = []
    for torre in estado.torres:
        torres.append(torre.copy())

    aux = torres[origem].pop()
    torres[destino].append(aux)

    return Estado(torres, estado)


def transfere_0_1(estado):
    return transfere(estado, 0, 1)


def transfere_1_2(estado):
    return transfere(estado, 1, 2)


def transfere_1_0(estado):
    return transfere(estado, 1, 0)


def transfere_2_1(estado):
    return transfere(estado, 2, 1)


def expande(estado):
    filhos = []
    transfs = [
        [0, 1],
        [1, 0],
        [1, 2],
        [2, 1],
        [0, 2],
        [2, 0],
    ]

    for transf in transfs:
        filho = transfere(estado, transf[0], transf[1])
        if filho != None and valido(filho):
            filhos.append(filho)

    return filhos


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
