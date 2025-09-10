import math

# Lendo valores
n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

# Calculando a combinação
if n < 0 or k < 0:
    print("Os valores devem ser não negativos.")
elif n < k:
    print(f"C({n}, {k}) = 0 (não é possível escolher mais elementos do que existem).")
else:
    combinacao = math.comb(n, k)  # disponível no Python 3.8+
    print(f"C({n}, {k}) = {combinacao}")
