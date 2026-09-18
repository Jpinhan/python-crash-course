convidados = ["mãe", "pai", "irmão"]
print(convidados[0].title() + ", Vamos jantar?")
print(convidados[1].title() + ", Vamos jantar?")
print(convidados[2].title() + ", Vamos jantar?")
print("\nMeu "+ convidados[2]+ " não vai poder comparecer, porque surgiu um imprevisto.\n")
convidados[2] = "vó"
print(convidados[0].title() + ", Vamos jantar?")
print(convidados[1].title() + ", Vamos jantar?")
print(convidados[2].title() + ", Vamos jantar?\n")
print(convidados[0].title() +", "+ convidados[1].title() +" e "+ convidados[2].title()+", encontrei uma mesa maior, poderei convidar mais 3 pessoas!" )
convidados.insert(0, "Vô")
convidados.insert(2, "tia")
convidados.append("tio")
print(convidados)
print(convidados[0].title() + ", Vamos jantar?")
print(convidados[1].title() + ", Vamos jantar?")
print(convidados[2].title() + ", Vamos jantar?")
print(convidados[3].title() + ", Vamos jantar?")
print(convidados[4].title() + ", Vamos jantar?")
print(convidados[5].title() + ", Vamos jantar?\n")
print(convidados[0].title() + ", " +convidados[1].title() + " ," + convidados[2].title() + ", " + convidados[3].title() + " ," + convidados[4].title() + " e " +convidados[5].title() +
      ", me desculpe pessoal, poderei levar apenas duas pessoas, meu pai e minha mãe.")
convidados_pop = convidados.pop(5)
print(convidados_pop.title() +" Me desculpe, por ter desmarcado o jantar")
convidados_pop = convidados.pop(4)
print(convidados_pop.title() +" Me desculpe, por ter desmarcado o jantar")
convidados_pop = convidados.pop(2)
print(convidados_pop.title() +" Me desculpe, por ter desmarcado o jantar")
convidados_pop = convidados.pop(0)
print(convidados_pop.title() +" Me desculpe, por ter desmarcado o jantar \n")
print(convidados[0].title() + " e " + convidados[1].title() + ", vocês ainda estão convidados para o jantar!")
print(convidados)
del convidados[0]
del convidados[0]
print(convidados)




