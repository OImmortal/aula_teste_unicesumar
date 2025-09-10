def lerDivisor(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def main():
    numero = int(input("Digite um número: "))
    divisores = lerDivisor(numero)
    print(f"Os divisores de {numero} são: {divisores}")

if __name__ == "__main__":
    main()