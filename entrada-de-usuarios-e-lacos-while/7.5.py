prompt = "Qual é a sua idade? (digite 'quit' para encerrar) "
programa_ativo = True

while programa_ativo:
    resposta = input(prompt)
    if resposta == 'quit':
        programa_ativo = False
    else:
        resposta = int(resposta)

        if resposta < 3:
            print("A entrada é gratuíta!")
        elif resposta < 12:
            print("A entrada é 10 dólares")
        else:
            print("A entrada é 15 dólares")
