qtd = int(input("Quantas notas?"))

if qtd <= 0:
    print("Quantidade inválida!")
else:
    soma = 0
    for _ in range(qtd):
        soma += float(input("Nota:"))

    media = soma / qtd
    print(f"Média: {media:.2f}")