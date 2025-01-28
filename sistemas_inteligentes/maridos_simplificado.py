from algoritmos_de_busca.bl_fronteira import bl


class Estado:
    def __init__(self, m1, e1, m2, e2, m3, e3, barco, pai):
        self.m1 = m1
        self.e1 = e1
        self.m2 = m2
        self.e2 = e2
        self.m3 = m3
        self.e3 = e3
        self.barco = barco
        self.pai = pai


def estado_inicial():
    return Estado(0, 0, 0, 0, 0, 0, 0, None)


def estado_objetivo(estado):
    return (
        estado.m1 == 1
        and estado.e1 == 1
        and estado.m2 == 1
        and estado.e2 == 1
        and estado.m3 == 1
        and estado.e3 == 1
        and estado.barco == 1
    )


def exibe(estado):
    barco = estado.barco
    exibicao = ""

    if barco == 1:
        barco = "| *|"
    else:
        barco = "|* |"

    exibicao += barco

    if estado.m1 == 1:
        exibicao = exibicao + f" m1:{estado.m1}"

    else:
        exibicao = f"m1:{estado.m1} " + exibicao

    if estado.e1 == 1:
        exibicao = exibicao + f" e1:{estado.e1}"
    else:
        exibicao = f"e1:{estado.e1} " + exibicao

    if estado.m2 == 1:
        exibicao = exibicao + f" m2:{estado.m2}"
    else:
        exibicao = f"m2:{estado.m2} " + exibicao

    if estado.e2 == 1:
        exibicao = exibicao + f" e2:{estado.e2}"
    else:
        exibicao = f"e2:{estado.e2} " + exibicao

    if estado.m3 == 1:
        exibicao = exibicao + f" m3:{estado.m3}"
    else:
        exibicao = f"m3:{estado.m3} " + exibicao

    if estado.e3 == 1:
        exibicao = exibicao + f" e3:{estado.e3}"
    else:
        exibicao = f"e3:{estado.e3} " + exibicao

    print(exibicao)


def valido(estado):
    if estado.e1 != estado.m1:
        if estado.m2 == estado.e1 or estado.m3 == estado.e1:
            return False

    if estado.e2 != estado.m2:
        if estado.m1 == estado.e2 or estado.m3 == estado.e2:
            return False

    if estado.e3 != estado.m3:
        if estado.m1 == estado.e3 or estado.m2 == estado.e3:
            return False

    return True


def levar(estado, m1, e1, m2, e2, m3, e3):
    if estado.barco == 1:
        if m1 == 1 and estado.m1 == 0:
            return None
        if e1 == 1 and estado.e1 == 0:
            return None
        if m2 == 1 and estado.m2 == 0:
            return None
        if e2 == 1 and estado.e2 == 0:
            return None
        if m3 == 1 and estado.m3 == 0:
            return None
        if e3 == 1 and estado.e3 == 0:
            return None
    else:
        if m1 == 1 and estado.m1 == 1:
            return None
        if e1 == 1 and estado.e1 == 1:
            return None
        if m2 == 1 and estado.m2 == 1:
            return None
        if e2 == 1 and estado.e2 == 1:
            return None
        if m3 == 1 and estado.m3 == 1:
            return None
        if e3 == 1 and estado.e3 == 1:
            return None

    if m1 == 1:
        m1 = 1 - estado.m1
    if e1 == 1:
        e1 = 1 - estado.e1
    if m2 == 1:
        m2 = 1 - estado.m2
    if e2 == 1:
        e2 = 1 - estado.e2
    if m3 == 1:
        m3 = 1 - estado.m3
    if e3 == 1:
        e3 = 1 - estado.e3

    barco = 1 - estado.barco
    if barco == estado.barco:
        return None

    return Estado(
        m1 if m1 is not None else estado.m1,
        e1 if e1 is not None else estado.e1,
        m2 if m2 is not None else estado.m2,
        e2 if e2 is not None else estado.e2,
        m3 if m3 is not None else estado.m3,
        e3 if e3 is not None else estado.e3,
        barco,
        estado,
    )


def expande(estado):
    movimentos = [
        [None, 1, None, None, None, None],  # esposa 1
        [None, None, None, 1, None, None],  # esposa 2
        [None, None, None, None, None, 1],  # esposa 3
        # ...
        [1, None, None, None, None, None],  # marido 1
        [None, None, 1, None, None, None],  # marido 2
        [None, None, None, None, 1, None],  # marido 3
        # ...
        [1, 1, None, None, None, None],  # casal 1
        [None, None, 1, 1, None, None],  # casal 2
        [None, None, None, None, 1, 1],  # casal 3
        # ...
        [1, None, 1, None, None, None],  # marido 1 e o marido 2
        [1, None, None, None, 1, None],  # marido 1 e o marido 3
        [None, None, 1, None, 1, None],  # marido 2 e o marido 3
        # ...
        [None, 1, None, 1, None, None],  # esposa 1 e a esposa 2
        [None, 1, None, None, None, 1],  # esposa 1 e a esposa 3
        [None, None, None, 1, None, 1],  # esposa 2 e a esposa 3
    ]

    filhos = []
    for movimento in movimentos:
        filho = levar(estado, *movimento)
        if filho is not None and valido(filho):
            filhos.append(filho)

    return filhos


def iguais(estado1, estado2):
    return (
        estado1.m1 == estado2
        and estado1.e1 == estado2.e1
        and estado1.m2 == estado2.m2
        and estado1.e2 == estado2.e2
        and estado1.m3 == estado2.m3
        and estado1.e3 == estado2.e3
        and estado1.barco == estado2.barco
    )


bl(exibe, estado_inicial, estado_objetivo, expande, iguais)
