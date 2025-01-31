Três maridos, com suas respectivas esposas, querem atravessar um rio. Acontece que, no barco só cabem duas pessoas e os 3 maridos são muito 
ciumentos e não permitem que sua esposa fique numa das margens com outro homem, sem que ele também esteja presente. Como pode ser feita a 
travessia sem utilizar veículo aéreo nem nadar? (Barbosa, 1999).

Escreva em pseudo-código uma classe para representar um estado desse problema. Use apenas tipos numéricos ou booleano.
Para cada membro da classe, diga que valor ou quantidade do estado do problema, esse membro representa (em forma de comentário).
Caso algum membro possa representar uma característica que pode assumar uma pequena quantidade de valores diferentes (enumerados),
diga o significado de cada um dos possíveis valores.
```
class Estado:
    def __init__(self, esquerda, direita, barco):
        # Esquerda e direita são listas de listas de inteiros
        # A primeira sub lista representa o primeiro casal, sendo o marido na primeira
        # posição e a esposa na segunda, e assim por diante
        # A segunda sub lista representa o segundo casal, e a terceira sub lista o terceiro casal

        self.esquerda = esquerda # quantidade de pessoas na margem esquerda
        # Exemplo: [[0, 0], [0, 0], [0, 0]] indica que todos estão na esquerda

        self.direita = direita # quantidade de pessoas na margem direita
        # Exemplo: [[1, 1], [1, 1], [1, 1]] indica que todos estão na direita

        self.barco = barco
        # 0 se o barco está na margem esquerda, 1 se está na margem direita
```

Escreva em pseudo-código uma função que retorna o estado inicial desse problema.
```
def estado_inicial():
    return Estado([[1, 1], [1, 1], [1, 1]], [[0, 0], [0, 0], [0, 0]], 0)
```

Escreva em pseudo-código uma função que retorne verdadeiro caso um estado seja um estado objetivo desse problema.
```
def objetivo(estado):
    return (
        estado.esquerda = [[0, 0], [0, 0], [0, 0]]
        and estado.direita == [[1, 1], [1, 1], [1, 1]]
        and estado.barco == 1
    )
```

Escreva em pseudo-código uma função que retorne verdadeiro caso um estado seja um estado válido desse problema.
```
def valido(estado):
    e1_esq = estado.esquerda[0][1]
    m1_esq = estado.esquerda[0][0]

    e2_esq = estado.esquerda[1][1]
    m2_esq = estado.esquerda[1][0]

    e3_esq = estado.esquerda[2][1]
    m3_esq = estado.esquerda[2][0]

    if e1_esq != m1_esq:
        if m2_esq == e1_esq or m3_esq == e1_esq:
            return False

    if e2_esq != m2_esq:
        if m1_esq == e2_esq or m3_esq == e2_esq:
            return False

    if e3_esq != m3_esq:
        if m1_esq == e3_esq or m2_esq == e3_esq:
            return False

    e1_dir = estado.direita[0][1]
    m1_dir = estado.direita[0][0]

    e2_dir = estado.direita[1][1]
    m2_dir = estado.direita[1][0]

    e3_dir = estado.direita[2][1]
    m3_dir = estado.direita[2][0]

    if e1_dir != m1_dir:
        if m2_dir == e1_dir or m3_dir == e1_dir:
            return False

    if e2_dir != m2_dir:
        if m1_dir == e2_dir or m3_dir == e2_dir:
            return False

    if e3_dir != m3_dir:
        if m1_dir == e3_dir or m2_dir == e3_dir:
            return False

    return True
```

```
def valido(estado):
    se e1 está em uma margem diferente de m1:
        se m2 ou m3 está na mesma margem que e1:
            retorne falso

    se e2 está em uma margem diferente de m2:
        se m1 ou m3 está na mesma margem que e2:
            retorne falso

    se e3 está em uma margem diferente de m3:
        se m1 ou m2 está na mesma margem que e3:
            retorne falso

    retorne verdadeiro
```

Escreva uma função que implementa a ação de levar uma das mulheres para a outra margem.
```
def leva_esposa1(estado):
    se barco está na esquerda e e1 está na esquerda:
        retorne novo estado com e1 na direita e todos os outros inalterados
    se nao:
        retorne vazio
    
    se barco está na direita e e1 está na direita:
        retorne novo estado com e1 na esquerda e todos os outros inalterados
    se nao:
        retorne vazio
```