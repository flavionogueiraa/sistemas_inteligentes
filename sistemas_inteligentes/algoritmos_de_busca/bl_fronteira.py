def bl(exibe, estado_inicial, objetivo, expande, iguais):
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

    def em_ancestrais(filho):
        ancestral = filho.pai
        while ancestral is not None:
            if iguais(filho, ancestral):
                return True

            ancestral = ancestral.pai

        return False

    def esta_na_fronteira(filho):
        for estado in fronteira:
            if iguais(estado, filho):
                return True

        return False

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
            if not esta_na_fronteira(filho) and not em_ancestrais(filho):
                adc_na_fronteira(filho)
