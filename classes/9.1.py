class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"o restaurante {self.restaurant_name} tem {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name} está aberto!")
restaurant = Restaurant("Mirazur","Cozinha Francesa")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
