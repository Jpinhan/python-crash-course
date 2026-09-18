convidados = ["mãe", "pai", "irmão"]
print(convidados[0].title() + ", Vamos jantar?")
print(convidados[1].title() + ", Vamos jantar?")
print(convidados[2].title() + ", Vamos jantar?")
print("\nMeu "+ convidados[2]+ " não vai poder comparecer, porque surgiu um imprevisto.\n")
convidados[2] = "Minha vozinha"
print(convidados[0].title() + ", Vamos jantar?")
print(convidados[1].title() + ", Vamos jantar?")
print(convidados[2].title() + ", Vamos jantar?")