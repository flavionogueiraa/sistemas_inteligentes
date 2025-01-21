from copy import deepcopy


def acao_encher_b5l(estado: dict):
    """Enche o primeiro balde."""
    novo_estado = deepcopy(estado)
    novo_estado["b5l"]["volume_atual"] = novo_estado["b5l"]["volume_maximo"]
    print(f"""{novo_estado['b5l']["nome"]} cheio""")
    return novo_estado


def acao_encher_b4l(estado: dict):
    """Enche o segundo balde."""
    novo_estado = deepcopy(estado)
    novo_estado["b4l"]["volume_atual"] = novo_estado["b4l"]["volume_maximo"]
    print(f"""{novo_estado['b4l']["nome"]} cheio""")
    return novo_estado


def acao_esvaziar_b5l(estado: dict):
    """Esvazia o primeiro balde."""
    novo_estado = deepcopy(estado)
    novo_estado["b5l"]["volume_atual"] = 0
    print(f"""{novo_estado['b5l']["nome"]} vazio""")
    return novo_estado


def acao_esvaziar_b4l(estado: dict):
    """Esvazia o segundo balde."""
    novo_estado = deepcopy(estado)
    novo_estado["b4l"]["volume_atual"] = 0
    print(f"""{novo_estado['b4l']["nome"]} vazio""")
    return novo_estado


def acao_transferir_b5l_para_b4l(estado: dict):
    """Transfere água do balde 1 para o balde 2."""
    novo_estado = deepcopy(estado)
    volume_disponivel = (
        novo_estado["b4l"]["volume_maximo"]
        - novo_estado["b4l"]["volume_atual"]
    )

    if novo_estado["b5l"]["volume_atual"] <= volume_disponivel:
        novo_estado["b4l"]["volume_atual"] += novo_estado["b5l"][
            "volume_atual"
        ]
        novo_estado["b5l"]["volume_atual"] = 0
    else:
        novo_estado["b5l"]["volume_atual"] -= volume_disponivel
        novo_estado["b4l"]["volume_atual"] = novo_estado["b4l"][
            "volume_maximo"
        ]
    print(
        f"""Transferência de {novo_estado['b5l']["nome"]} para {estado['b4l']["nome"]}"""  # noqa E501
    )
    return novo_estado


def acao_transferir_b4l_para_b5l(estado: dict):
    """Transfere água do balde 2 para o balde 1."""
    novo_estado = deepcopy(estado)
    volume_disponivel = (
        novo_estado["b5l"]["volume_maximo"] - estado["b5l"]["volume_atual"]
    )

    if novo_estado["b4l"]["volume_atual"] <= volume_disponivel:
        novo_estado["b5l"]["volume_atual"] += novo_estado["b4l"][
            "volume_atual"
        ]
        novo_estado["b4l"]["volume_atual"] = 0
    else:
        novo_estado["b4l"]["volume_atual"] -= volume_disponivel
        novo_estado["b5l"]["volume_atual"] = novo_estado["b5l"][
            "volume_maximo"
        ]
    print(
        f"""Transferência de {novo_estado['b4l']["nome"]} para {estado['b5l']["nome"]}"""  # noqa E501
    )
    return novo_estado


def objetivo_alcancado(estado: dict):
    """
    Verifica se o objetivo foi alcançado.
    Objetivo: A soma dos volumes é igual a 3.
    """
    atingiu = (
        estado["b5l"]["volume_atual"] + estado["b4l"]["volume_atual"] == 3
    )
    atingiu_sim_nao = "Sim" if atingiu else "Não"
    print(f"Objetivo alcançado: {atingiu_sim_nao}")


def representar_estado(estado: dict):
    """Representa o estado atual dos baldes."""
    print("Estado dos baldes:")
    print(
        f"""{estado['b5l']["nome"]}: {estado['b5l']["volume_atual"]}/{estado['b5l']["volume_maximo"]}"""  # noqa E501
    )
    print(
        f"""{estado['b4l']["nome"]}: {estado['b4l']["volume_atual"]}/{estado['b4l']["volume_maximo"]}"""  # noqa E501
    )


def expandir_estado(estado_pai: dict):
    """Expande o estado atual."""
    acoes = [
        acao_encher_b5l,
        acao_encher_b4l,
        acao_esvaziar_b5l,
        acao_esvaziar_b4l,
        acao_transferir_b5l_para_b4l,
        acao_transferir_b4l_para_b5l,
    ]
    estados_filhos = []
    for acao in acoes:
        estado_filho = acao(estado_pai)
        if estado_filho not in estados_filhos:
            estados_filhos.append(estado_filho)

    print("Estado pai:")
    representar_estado(estado_pai)
    print("")

    print("Estados filhos:")
    for index, estado_filho in enumerate(estados_filhos):
        print(f"Estado filho {index + 1}:")
        representar_estado(estado_filho)
        print("")


def solucao(estado: dict):
    """Encontra a solução do problema."""
    acoes_solucao = [
        acao_encher_b4l,
        acao_transferir_b4l_para_b5l,
        acao_encher_b4l,
        acao_transferir_b4l_para_b5l,
        acao_esvaziar_b5l,
        objetivo_alcancado,
    ]
    for acao in acoes_solucao:
        estado = acao(estado)


estado_baldes = {
    "b5l": {
        "nome": "Balde 5L",
        "volume_maximo": 5,
        "volume_atual": 0,
    },
    "b4l": {
        "nome": "Balde 4L",
        "volume_maximo": 4,
        "volume_atual": 0,
    },
}

# solucao(estado_baldes)
# expandir_estado(estado_baldes)

representar_estado(estado_baldes)
objetivo_alcancado(estado_baldes)
print("")

estado_baldes = acao_encher_b4l(estado_baldes)
representar_estado(estado_baldes)
objetivo_alcancado(estado_baldes)
print("")

estado_baldes = acao_transferir_b4l_para_b5l(estado_baldes)
representar_estado(estado_baldes)
objetivo_alcancado(estado_baldes)
print("")

estado_baldes = acao_encher_b4l(estado_baldes)
representar_estado(estado_baldes)
objetivo_alcancado(estado_baldes)
print("")

estado_baldes = acao_transferir_b4l_para_b5l(estado_baldes)
representar_estado(estado_baldes)
objetivo_alcancado(estado_baldes)
print("")

estado_baldes = acao_esvaziar_b5l(estado_baldes)
representar_estado(estado_baldes)
objetivo_alcancado(estado_baldes)
print("")
