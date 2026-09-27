#algo = ""
#while sabores != "quit":
#    algo = input(sabores)
#    if algo != "quit":
#        print(algo)

#sabores = "Qual sabor você deseja?digite quit para sair"
#active = True
#while active:
#    message = input(sabores)
#    if message == "quit":
#        active = False
#    else:
#        print(message)



sabores = "Qual sabor você deseja? Digite quit para sair"
sabor = ""
while True:
    sabor = input(sabores)
    if sabor == "quit":
        break
    else:
        print(f"{sabor} foi adicionado")