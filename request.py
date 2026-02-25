import requests

nome = input("Digite um número ou nome do Pokémon: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    print("Nome:", dados["name"].capitalize())
    print("ID:", dados["id"])
    print("Tipo(s):", ", ".join([t['type']['name'].capitalize() for t in dados['types']]))
else:
    print("Pokémon não encontrado! Verifique o número ou nome digitado.")
