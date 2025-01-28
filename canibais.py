from algoritmos_de_busca.bp_ancestrais import bp


class Estado:
    def __init__(self, ce, me, cd, md, barco, pai):
        self.ce = ce
        self.me = me
        self.cd = cd
        self.md = md
        self.barco = barco
        self.nivel = 0 if pai is None else pai.nivel + 1
        self.pai = pai


def exibe(estado):
    barco = "* "
    if estado.barco == 0:
        barco = " *"
    print(f"{estado.ce} {estado.me}|{barco}| {estado.cd} {estado.md}")


def estado_inicial():
    return Estado(0, 0, 3, 3, 0, None)


def objetivo(estado):
    return estado.me == 3 and estado.ce == 3


def valido(estado):
    if estado.me > 0:
        if estado.ce > estado.me:
            return False

    if estado.md > 0:
        if estado.cd > estado.md:
            return False

    if estado.md < 0 or estado.me < 0:
        return False

    if estado.cd < 0 or estado.ce < 0:
        return False

    return True


def transfere(estado, qtd_canibais, qtd_missionarios):
    # Se o barco estiver na direita
    if estado.barco == 0:
        qtd_canibais = -qtd_canibais
        qtd_missionarios = -qtd_missionarios

    me = estado.me - qtd_missionarios
    ce = estado.ce - qtd_canibais
    md = estado.md + qtd_missionarios
    cd = estado.cd + qtd_canibais

    return Estado(ce, me, cd, md, 1 - estado.barco, estado)


def transfere_1_canibal(estado):
    return transfere(estado, 1, 0)


def transfere_1_missionario(estado):
    return transfere(estado, 0, 1)


def transfere_2_canibais(estado):
    return transfere(estado, 2, 0)


def transfere_2_missionarios(estado):
    return transfere(estado, 0, 2)


def transfere_1_canibal_1_missionario(estado):
    return transfere(estado, 1, 1)


def expande(estado):
    filhos = []

    filho = transfere_1_canibal(estado)
    if valido(filho):
        filhos.append(filho)

    filho = transfere_1_missionario(estado)
    if valido(filho):
        filhos.append(filho)

    filho = transfere_2_canibais(estado)
    if valido(filho):
        filhos.append(filho)

    filho = transfere_2_missionarios(estado)
    if valido(filho):
        filhos.append(filho)

    filho = transfere_1_canibal_1_missionario(estado)
    if valido(filho):
        filhos.append(filho)

    return filhos


def iguais(estado1, estado2):
    return (
        estado1.ce == estado2.ce
        and estado1.me == estado2.me
        and estado1.cd == estado2.cd
        and estado1.md == estado2.md
        and estado1.barco == estado2.barco
    )


bp(exibe, estado_inicial, objetivo, expande, iguais)

visitados = 4 * [4 * [2 * [0]]]
