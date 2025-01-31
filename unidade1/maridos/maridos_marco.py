class Estado:
    def __init__(self, homens, mulheres, barco, pai):
        # Vetor representando os homens
        # se homens[i] = 0, então o i-ésimo homem
        # está na margem esquerda, caso contrário,
        # está na margem direita
        self.homens = homens
        # Idem
        self.mulheres = mulheres
        # Idem
        self.barco = barco
        self.pai = pai


def estado_inicial():
    return Estado([0, 0, 0], [0, 0, 0], 0, None)


def objetivo(estado):
    return (
        estado.homens == [1, 1, 1]
        and estado.mulheres == [1, 1, 1]
        and estado.barco == 1
    )


def exibe(estado):
    # linha0 = " 0 1 2 |  |     "
    # linha1 = "       |* |     "
    # linha2 = " 0 1 2 |  |     "

    # if estado.barco == 1:
    #     linha1 = "       | *|     "

    # for i in range(len(estado.mulheres)):
    #     if estado.mulheres[i] == 1:
    #         linha0[2 * i + 1] = " "
    #         linha0[2 * i + 13] = "012"[i]

    # for i in range(len(estado.homens)):
    #     if estado.homens[i] == 1:
    #         linha2[2 * i + 1] = " "
    #         linha2[2 * i + 13] = "012"[i]

    # print(linha0)
    # print(linha1)
    # print(linha2)

    for i in range(len(estado.mulheres)):
        print(" ", end="")
        if estado.mulheres[i] == 0:
            print(i, end="")
        else:
            print(" ", end="")
    print("|   |", end="")
    for i in range(len(estado.mulheres)):
        print(" ", end="")
        if estado.mulheres[i] == 1:
            print(i, end="")
        else:
            print(" ", end="")

    print()
    linha1 = "      |*  |     "
    if estado.barco == 1:
        linha1 = "       |  *|     "
    print(linha1)

    for i in range(len(estado.homens)):
        print(" ", end="")
        if estado.homens[i] == 0:
            print(i, end="")
        else:
            print(" ", end="")
    print("|   |", end="")
    for i in range(len(estado.homens)):
        print(" ", end="")
        if estado.homens[i] == 1:
            print(i, end="")
        else:
            print(" ", end="")

    print()


def valido(estado):
    for i in range(len(estado.mulheres)):
        if estado.mulheres[i] == estado.homens[i]:
            continue

        for j in range(len(estado.homens)):
            if estado.mulheres[i] == estado.homens[j]:
                return False

    return True


def expande(estado):
    filhos = []

    # Transportar uma mulher:
    for i in range(len(estado.mulheres)):
        if estado.mulheres[i] != estado.barco:
            continue
        mulheres = estado.mulheres.copy()
        mulheres[i] = 1 - mulheres[i]
        filho = Estado(
            estado.homens.copy(), mulheres, 1 - estado.barco, estado
        )
        if valido(filho):
            filhos.append(filho)

    # Transportar duas mulheres:
    for i in range(len(estado.mulheres)):
        for j in range(i, len(estado.mulheres)):
            if i == j:
                continue

            if estado.mulheres[i] != estado.barco:
                continue

            if estado.mulheres[j] != estado.barco:
                continue

            mulheres = estado.mulheres.copy()
            mulheres[i] = 1 - mulheres[i]
            mulheres[j] = 1 - mulheres[j]

            filho = Estado(
                estado.homens.copy(), mulheres, 1 - estado.barco, estado
            )
            if valido(filho):
                filhos.append(filho)

    # Transportar um homem:
    for i in range(len(estado.homens)):
        if estado.homens[i] != estado.barco:
            continue
        homens = estado.homens.copy()
        homens[i] = 1 - homens[i]
        filho = Estado(
            homens, estado.mulheres.copy(), 1 - estado.barco, estado
        )
        if valido(filho):
            filhos.append(filho)

    # Transportar dois homens:
    for i in range(len(estado.homens)):
        for j in range(i, len(estado.homens)):
            if i == j:
                continue

            if estado.homens[i] != estado.barco:
                continue

            if estado.homens[j] != estado.barco:
                continue

            homens = estado.homens.copy()
            homens[i] = 1 - homens[i]
            homens[j] = 1 - homens[j]

            filho = Estado(
                homens, estado.mulheres.copy(), 1 - estado.barco, estado
            )
            if valido(filho):
                filhos.append(filho)

    # Transportar um casal:
    for i in range(len(estado.homens)):
        if (
            estado.homens[i] != estado.barco
            and estado.mulheres[i] != estado.barco
        ):
            continue
        homens = estado.homens.copy()
        mulheres = estado.mulheres.copy()

        homens[i] = 1 - homens[i]
        mulheres[i] = 1 - mulheres[i]

        filho = Estado(homens, mulheres, 1 - estado.barco, estado)
        if valido(filho):
            filhos.append(filho)

    return filhos
