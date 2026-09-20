pizzas = ["mussarela", "Calabresa", "frango com catupiry", "Marguerita"]
for pizza in pizzas:
    print("Pizza de "+pizza.title() + " é boa!")
    print("Mas eu prefiro de Brigadeiro!\n")

print("Infelizmente eu estou de dieta e faz meses que eu não como pizza")
pizzas = ["mussarela", "Calabresa", "frango com catupiry", "Marguerita"]
friend_pizzas = ["mussarela", "Calabresa", "frango com catupiry", "Marguerita"]
pizzas.append("quatro queijos")
friend_pizzas.append("File Mignon")
print(f"Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)
print(f"As pizzas favoritas do meu amigo são:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)



