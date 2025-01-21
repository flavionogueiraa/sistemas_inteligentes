class Estado:
    qtd_c_margem_e = 0
    qtd_c_margem_d = 0
    qtd_m_margem_e = 0
    qtd_m_margem_d = 0
    posicao_barco = ""

    def __init__(
        self,
        qtd_c_margem_e,
        qtd_m_margem_e,
        qtd_c_margem_d,
        qtd_m_margem_d,
        posicao_barco,
    ):
        self.qtd_c_margem_e = qtd_c_margem_e
        self.qtd_m_margem_e = qtd_m_margem_e
        self.qtd_c_margem_d = qtd_c_margem_d
        self.qtd_m_margem_d = qtd_m_margem_d
        self.posicao_barco = posicao_barco


def estado_inicial():
    """Retorna o estado inicial do problema."""
    return Estado(0, 0, 3, 3, "d")


def estado_objetivo(estado: Estado):
    """Retorna o estado objetivo do problema."""
    return estado.qtd_c_margem_e == 3 and estado.qtd_m_margem_e == 3


def acao_levar_c_d_para_e(estado: Estado):
    """Leva um canibal da margem direita para a margem esquerda."""
    if not estado.posicao_barco == "d":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e + 1,
        estado.qtd_m_margem_e,
        estado.qtd_c_margem_d - 1,
        estado.qtd_m_margem_d,
        posicao_barco="e",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar_c_e_para_d(estado: Estado):
    """Leva um canibal da margem esquerda para a margem direita."""
    if not estado.posicao_barco == "e":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e - 1,
        estado.qtd_m_margem_e,
        estado.qtd_c_margem_d + 1,
        estado.qtd_m_margem_d,
        posicao_barco="d",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar_m_d_para_e(estado: Estado):
    """Leva um missionário da margem direita para a margem esquerda."""
    if not estado.posicao_barco == "d":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e,
        estado.qtd_m_margem_e + 1,
        estado.qtd_c_margem_d,
        estado.qtd_m_margem_d - 1,
        posicao_barco="e",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar_m_e_para_d(estado: Estado):
    """Leva um missionário da margem esquerda para a margem direita."""
    if not estado.posicao_barco == "e":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e,
        estado.qtd_m_margem_e - 1,
        estado.qtd_c_margem_d,
        estado.qtd_m_margem_d + 1,
        posicao_barco="d",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar2_c_d_para_e(estado: Estado):
    """Leva dois canibais da margem direita para a margem esquerda."""
    if not estado.posicao_barco == "d":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e + 2,
        estado.qtd_m_margem_e,
        estado.qtd_c_margem_d - 2,
        estado.qtd_m_margem_d,
        posicao_barco="e",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar2_c_e_para_d(estado: Estado):
    """Leva dois canibais da margem esquerda para a margem direita."""
    if not estado.posicao_barco == "e":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e - 2,
        estado.qtd_m_margem_e,
        estado.qtd_c_margem_d + 2,
        estado.qtd_m_margem_d,
        posicao_barco="d",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar2_m_d_para_e(estado: Estado):
    """Leva dois missionários da margem direita para a margem esquerda."""
    if not estado.posicao_barco == "d":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e,
        estado.qtd_m_margem_e + 2,
        estado.qtd_c_margem_d,
        estado.qtd_m_margem_d - 2,
        posicao_barco="e",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar2_m_e_para_d(estado: Estado):
    """Leva dois missionários da margem esquerda para a margem direita."""
    if not estado.posicao_barco == "e":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e,
        estado.qtd_m_margem_e - 2,
        estado.qtd_c_margem_d,
        estado.qtd_m_margem_d + 2,
        posicao_barco="d",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar_cm_d_para_e(estado: Estado):
    """Leva um canibal e um missionário da margem direita para a margem esquerda."""  # noqa E501
    if not estado.posicao_barco == "d":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e + 1,
        estado.qtd_m_margem_e + 1,
        estado.qtd_c_margem_d - 1,
        estado.qtd_m_margem_d - 1,
        posicao_barco="e",
    )
    if not estado_valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def acao_levar_cm_e_para_d(estado: Estado):
    """Leva um canibal e um missionário da margem esquerda para a margem direita."""  # noqa E501
    if not estado.posicao_barco == "e":
        print("Ação não executada!")
        return None

    estado_ = Estado(
        estado.qtd_c_margem_e - 1,
        estado.qtd_m_margem_e - 1,
        estado.qtd_c_margem_d + 1,
        estado.qtd_m_margem_d + 1,
        posicao_barco="d",
    )
    if not estado_valido(estado_):
        print("Ação impossível de ser feita!")
        return None
    if not valido(estado_):
        print("Ação não executada! Os canibais comeram os cabas!!")
        return None

    return estado_


def estado_valido(estado: Estado):
    """Verifica se o estado é válido."""
    return (
        estado.qtd_c_margem_e >= 0
        and estado.qtd_m_margem_e >= 0
        and estado.qtd_c_margem_d >= 0
        and estado.qtd_m_margem_d >= 0
    )


def valido(estado: Estado):
    """Verifica se o estado é restrito."""
    if estado.qtd_m_margem_e > 0:
        if estado.qtd_c_margem_e > estado.qtd_m_margem_e:
            return False
    if estado.qtd_m_margem_d > 0:
        if estado.qtd_c_margem_d > estado.qtd_m_margem_d:
            return False

    return True


def expandir(estado: Estado):
    """Expande o estado."""
    filhos = []
    if estado.posicao_barco == "d":
        filho = acao_levar_c_d_para_e(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar_m_d_para_e(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar2_c_d_para_e(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar2_m_d_para_e(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar_cm_d_para_e(estado)
        if filho and valido(filho):
            filhos.append(filho)
    else:
        filho = acao_levar_c_e_para_d(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar_m_e_para_d(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar2_c_e_para_d(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar2_m_e_para_d(estado)
        if filho and valido(filho):
            filhos.append(filho)
        filho = acao_levar_cm_e_para_d(estado)
        if filho and valido(filho):
            filhos.append(filho)

    for filho in filhos:
        representar_estado(filho)
    return filhos


def representar_estado(estado: Estado):
    """Representa o estado do problema."""
    margem_esquerda = f"{estado.qtd_c_margem_e}C {estado.qtd_m_margem_e}M"
    margem_direita = f"{estado.qtd_c_margem_d}C {estado.qtd_m_margem_d}M"

    margem_meio = "| |"
    if estado.posicao_barco == "e":
        margem_meio = "|* |"
    elif estado.posicao_barco == "d":
        margem_meio = "| *|"

    print(f"{margem_esquerda} {margem_meio} {margem_direita}")


def solucao(estado: Estado):
    """Faz a solução do problema."""
    representar_estado(estado)
    estado = acao_levar2_c_d_para_e(estado)
    estado = acao_levar_c_e_para_d(estado)
    estado = acao_levar2_c_d_para_e(estado)
    estado = acao_levar_c_e_para_d(estado)
    estado = acao_levar2_m_d_para_e(estado)
    estado = acao_levar_cm_e_para_d(estado)
    estado = acao_levar2_m_d_para_e(estado)
    estado = acao_levar_c_e_para_d(estado)
    estado = acao_levar2_c_d_para_e(estado)
    estado = acao_levar_c_e_para_d(estado)
    estado = acao_levar2_c_d_para_e(estado)
    representar_estado(estado)


e = estado_inicial()
solucao(e)


def transfere(estado, qtd_canibais, qtd_missionarios):
    """Transfere canibais e missionários de uma margem para outra."""
    if estado.posicao_barco == "d":
        qtd_canibais = -qtd_canibais
        qtd_missionarios = -qtd_missionarios

    me = estado.qtd_c_margem_e - qtd_canibais
    md = estado.qtd_c_margem_d + qtd_canibais
    me_m = estado.qtd_m_margem_e - qtd_missionarios
    md_m = estado.qtd_m_margem_d + qtd_missionarios

    posicao_barco = "d" if estado.posicao_barco == "e" else "e"
    return Estado(me, me_m, md, md_m, posicao_barco)
