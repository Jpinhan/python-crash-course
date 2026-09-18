# a ideia aqui é fazer uma lista de uma pessoa que fez um pedido de whatsapp em um petshop
pedido = ["2 saches friskies carne", "1kg matisse ad salmão", "1 areia pipicat classic 4kg"]
#acessando elementos da lista
print(pedido[0])
print(pedido[1])
print(pedido[2])

#alterando um produto da lista
pedido[0] = "2 saches whiskas carne"
print(pedido[0])

#adicionando elemento na lista
pedido.append("Churu salmão e atum")
print(pedido)

#inserindo(escolher o lugar) elementos em uma lista
pedido.insert(3, "1 dreams carne 40g" )
print(pedido)

#removendo um item em uma lista
del pedido[4]
print(pedido)

#removendo um item em uma lista metodo pop(posso usar o item removido, sempre o ultimo)
item_pop = pedido.pop()
print(pedido)
print(item_pop)

#escolhendo um item para remover
item_pop = pedido.pop(0)
print(pedido)
print(item_pop)

#removendo um item de acordo com o valor
pedido.remove("1 areia pipicat classic 4kg")
print(pedido)

#ordenando a lista de forma permanente
pedido = ["2 saches friskies carne", "1kg matisse ad salmão", "1 areia pipicat classic 4kg"]
print(pedido)

pedido.sort()
print(pedido)

#ordenando uma lista temporariamente com a funcao sorted()
pedido = ["2 saches friskies carne", "1kg matisse ad salmão", "1 areia pipicat classic 4kg"]
print(sorted(pedido))
print(pedido)

#Exibindo uma lista em ordem inversa
pedido.reverse()
print(pedido)

#Descobrindo o tamanho de uma lista
print(len(pedido))
