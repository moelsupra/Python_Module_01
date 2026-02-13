# class Plant:
#     def __init__(self, name, height, age):
#         self.name = name
#         self.height = height
#         self.age = age
    
#     def grow(self):
#         self.height += 1

    
#     def age_one_day(self):
#         self.age += 1
#         print(f"{self.name} is now {self.age} days old!")

#     def water(self):
#         print(f"{self.name} has been watered!")
    
#     def get_info(self):
#         return f"{self.name}: {self.height}cm, {self.age} days old"

# # Test it:
# sunflower = Plant("Sunflower", 50, 40)
# sunflower.grow()
# sunflower.grow()
# sunflower.age_one_day()
# # sunflower.get_info()
# print(sunflower.height)









# # Parent class
# class Plant:
#     def __init__(self, name, height, age):
#         self.name = name
#         self.height = height
#         self.age = age
    
#     def grow(self):
#         self.height += 1
    
#     def get_info(self):
#         return f"{self.name}: {self.height}cm, {self.age} days"

# # TODO: Create a Cactus class that inherits from Plant
# class Cactus(Plant):
#     def __init__(self, name, height, age, water_storage):
#         super().__init__(name, height, age) 
#         self.water_storage = water_storage

#     def store_water(self):
#         print(f"Stores {self.water_storage} litres")
# # Additional attributes: water_storage (in liters)
# # Additional method: store_water() - prints how much water it stores

# # Test your Cactus:
# cactus = Cactus("Desert Cactus", 30, 200, 5)
# cactus.grow()
# cactus.store_water()
# print(cactus.get_info())

if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")