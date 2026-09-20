current_users = ["qwert", "qweqwe", "david", "alex", "mike"]

new_users = ["marco", "john", "mike", "alex", "maria"]

current_users_lower = [current_users.lower() for current_users in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"O nome de usuário {new_user} já está sendo usado, por favor, "
              f"por favor escolha outro nome ")
    else:
        print(f"Esse nome de usuário {new_user} está disponível")
