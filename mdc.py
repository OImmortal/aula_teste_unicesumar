def main():
    number1 = int(input("Digite o primeiro valor: "))
    number2 = int(input("Digite o segundo valor: "))

    minDivComun = minimoDivisorComun(n1=number1, n2=number2)
    print(f"O Mdc de {number1} e {number2} é {minDivComun}")

def minimoDivisorComun(n1, n2):
    while n2 != 0:
        temp = n2
        n2 = n1 % n2
        n1 = temp
    return n1

if __name__ == "__main__":
    main()