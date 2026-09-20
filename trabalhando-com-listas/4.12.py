my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\n")
print("My friend's favorite foods are:")
friend_foods = my_foods[:]
for food in friend_foods:
    print(food)

