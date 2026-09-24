favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'sarah', 'maria', 'joao', 'phil']

for person in people:
    if person in favorite_languages:
        print(f"Obrigado por responder à enquete, {person.title()}!")
    else:
        print(f"{person.title()}, por favor, responda à enquete.")