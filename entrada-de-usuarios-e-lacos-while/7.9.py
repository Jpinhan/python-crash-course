sandwich_orders = ["Pastrami", "Bauru", "Beirute", "Pastrami", "Misto Quente",
                   "Buraco ", "Pastrami", "X-Tudo", "Sanduíche de Pernil", "Xis Gaúcho"]

fineshed_sandwiches = []
print("\n")
print("Estamos sem Pastrami")
print("\n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Preparando seu sanduíche de {current_sandwich}.")
    fineshed_sandwiches.append(current_sandwich)

print("\nSanduíches preparados:")
for sandwich in fineshed_sandwiches:
    print(f"{sandwich}")
