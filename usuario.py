pessoa = {"nome": "João", "idade": 20}

chave = input("Qual campo quer ver? ").strip().lower()

valor = pessoa.get(chave, "Campo não encontrado!")
print(valor)