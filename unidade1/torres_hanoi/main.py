from copy import deepcopy


class Estado:
    torres = [[], [], []]

    def __init__(self, torres):
        self.torres = torres


def estado_inicial():
    return Estado([[3, 2, 1], [], []])


def exibe(estado):
    for index in range(2, -1, -1):
        for torre in estado.torres:
            try:
                disco = torre[index]
                print(disco, end="\t")
            except IndexError:
                print("|", end="\t")
        print("\t")


def transferir(estado, origem, destino):
    estado_ = deepcopy(estado)
    movimentos_invalidos = [
        origem < 0,
        origem > 2,
        destino < 0,
        destino > 2,
        origem == destino,
        destino == origem + 2,
        destino == origem - 2,
    ]
    if any(movimentos_invalidos):
        # print("Movimento inválido")
        return None

    torres = estado_.torres
    try:
        disco = torres[origem].pop()
    except IndexError:
        # print("Não há discos na torre de origem")
        return None

    if torres[destino]:
        if torres[destino][-1] < disco:
            # print("Um disco maior não pode ser colocado sobre um menor")
            return None

    torres[destino].append(disco)
    return Estado(torres)


def mover_pri_seg(estado):
    return transferir(estado, 0, 1)


def mover_seg_pri(estado):
    return transferir(estado, 1, 0)


def mover_seg_ter(estado):
    return transferir(estado, 1, 2)


def mover_ter_seg(estado):
    return transferir(estado, 2, 1)


def expandir(estado):
    filhos = []
    filho = mover_pri_seg(estado)
    if filho:
        filhos.append(filho)

    filho = mover_seg_pri(estado)
    if filho:
        filhos.append(filho)

    filho = mover_seg_ter(estado)
    if filho:
        filhos.append(filho)

    filho = mover_ter_seg(estado)
    if filho:
        filhos.append(filho)

    return filhos


def objetivo(estado):
    return estado.torres[2] == [3, 2, 1]


def solucao():
    estado = estado_inicial()
    exibe(estado)
    print("\n")

    acoes = [
        mover_pri_seg,
        mover_seg_ter,
        mover_pri_seg,
        mover_ter_seg,
        mover_seg_pri,
        mover_seg_ter,
        mover_pri_seg,
        mover_seg_ter,
        mover_pri_seg,
        mover_ter_seg,
        mover_seg_pri,
        mover_ter_seg,
        mover_pri_seg,
        mover_seg_ter,
        mover_seg_pri,
        mover_ter_seg,
        mover_seg_pri,
        mover_seg_ter,
        mover_pri_seg,
        mover_seg_ter,
        mover_pri_seg,
        mover_ter_seg,
        mover_seg_pri,
        mover_seg_ter,
        mover_pri_seg,
        mover_seg_ter,
    ]
    for acao in acoes:
        estado = acao(estado)
        exibe(estado)
        print("\n")

    print(objetivo(estado))
