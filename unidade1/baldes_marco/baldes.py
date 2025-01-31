class Estado:
    def __init__(self, v1, v2, pai):
        self.v1 = v1
        self.v2 = v2
        self.pai = pai


def exibe(estado):
    print(f"V1: {estado.v1} V2:{estado.v2}")


def estado_inicial():
    return Estado(0, 0, None)


def objetivo(estado):
    return estado.v1 + estado.v2 == 3


def encher_1(estado):
    return Estado(5, estado.v2, estado)


def encher_2(estado):
    return Estado(estado.v1, 4, estado)


def esvaziar_1(estado):
    return Estado(0, estado.v2, estado)


def esvaziar_2(estado):
    return Estado(estado.v1, 0, estado)


def transfere_1_2(estado):
    transf = 4 - estado.v2
    if estado.v1 <= transf:
        transf = estado.v1
    return Estado(estado.v1 - transf, estado.v2 + transf, estado)


def transfere_2_1(estado):
    transf = 5 - estado.v1
    if estado.v2 <= transf:
        transf = estado.v2
    return Estado(estado.v1 + transf, estado.v2 - transf, estado)


def expande(estado):
    filhos = []
    filhos.append(encher_1(estado))
    filhos.append(encher_2(estado))
    filhos.append(esvaziar_1(estado))
    filhos.append(esvaziar_2(estado))
    filhos.append(transfere_1_2(estado))
    filhos.append(transfere_2_1(estado))
    return filhos
