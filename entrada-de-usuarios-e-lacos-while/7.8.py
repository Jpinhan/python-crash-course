sandwich_orders = ["Bauru", "Beirute", "Misto Quente", "Buraco Quente",
                   "X-Tudo", "Sanduíche de Pernil", "Xis Gaúcho"]
finished_sandwiches = []

while sandwich_orders:
    preparados = sandwich_orders.pop()
    print(f"Preparei o seu sanduíche de {preparados}.")
    finished_sandwiches.append(preparados)
print("\n")
for sanduiche in finished_sandwiches:
    print(sanduiche)
