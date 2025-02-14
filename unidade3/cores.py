import math

tabela = [
    [40, 20, "Vermelho", 0],
    [50, 50, "Azul", 0],
    [60, 90, "Azul", 0],
    [10, 25, "Vermelho", 0],
]

k = 3
exemplo = [20, 35]

for item in tabela:
    item[3] = math.dist(exemplo, item[:2])

tabela.sort(key=lambda x: x[3])
k_primeiros = tabela[:k]

qtd_vermelhos = 0
qtd_azuis = 0

for item in k_primeiros:
    if item[2] == "Vermelho":
        qtd_vermelhos += 1
    else:
        qtd_azuis += 1

print(k_primeiros)
if qtd_vermelhos > qtd_azuis:
    print("Vermelho")
else:
    print("Azul")
