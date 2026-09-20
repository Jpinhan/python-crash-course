racao = "Premier"
print(racao == "premier")
print(racao == "premier".title())
print("\n")
racao = "formula natural"
print(racao == "FORMULA NATURAL".lower())
print(racao == "Formula natural")
print("\n")
peso = 80
print(peso <= 50)
print(20 <= peso <= 50)
print(peso >= 50)
print("\n")
idade = 27
idade_1 = 50
print(idade >= 18 and idade <= 40)
print(idade >= 28 and idade <= 40)
print(idade >= 20 or idade_1 <= 40 )
print(idade >= 28 or idade_1 <= 49)
print("\n")
list = ["premier", "formula natural", "guabi natural"]
print("premier" in list)
print("Guabi natural" in list)