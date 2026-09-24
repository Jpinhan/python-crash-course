rivers_1 = {"Amazonas": "Ele é o rio com o maior volume de água do planeta, despejando sozinho cerca de 20% de toda a água doce que vai para os oceanos no mundo."
                        "", "Nilo": "Ele é amplamente conhecido como o rio mais longo do mundo, com mais de 6.600 quilômetros de extensão"
                                    "", "Rio Yangtzé": "Ele abriga a Usina de Três Gargantas, a maior usina hidrelétrica do mundo. A obra é tão gigantesca que o peso da água acumulada alterou de forma sutil o eixo de rotação da Terra"}
rivers = {"Amazonas": "Brasil", "Nilo": "Egito", "Rio Yangtzé": "China"}

for river, phrase in rivers_1.items():
    print(f"{river}:\n{phrase}")
    print("\n")
for river, country in rivers.items():
    print(f"{river}")
print("\n")
for river, country in rivers.items():
    print(f"{country}")


