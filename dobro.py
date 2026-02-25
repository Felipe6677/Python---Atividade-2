def dobro(x):
    return float(x) * 2

valor = input("Digite um número:")

if valor == "":
    print("Você não digitou nenhum número.")
else:
    print(dobro(valor))