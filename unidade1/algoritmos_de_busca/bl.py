def bl(exibe, estado_inicial, objetivo, expande):
    fronteira = []

    def adc_na_fronteira(estado):
        fronteira.append(estado)

    def vazia():
        return fronteira == []

    def rmv_da_fronteira():
        return fronteira.pop(0)

    def mostrar_caminho(estado):
        if estado is None:
            return

        mostrar_caminho(estado.pai)
        exibe(estado)

    adc_na_fronteira(estado_inicial())
    while not vazia():
        atual = rmv_da_fronteira()
        exibe(atual)
        if objetivo(atual):
            print("Solução encontrada!")
            mostrar_caminho(atual)
            break

        filhos = expande(atual)
        for filho in filhos:
            adc_na_fronteira(filho)
