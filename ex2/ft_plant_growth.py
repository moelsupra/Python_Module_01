class Plant:
    """Represent a plant that can grow and age over time"""
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        """Increase plant height by 1cm"""
        self.height += 1

    def age(self) -> None:
        """Increase plant age by 1 day"""
        self.plant_age += 1

    def get_info(self) -> str:
        """Get plant information as a formatted string"""
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    tulip = Plant("Tulip", 15, 10)
    sunflower = Plant("Sunflower", 40, 20)

    plants = [rose, tulip, sunflower]

    initial_heights = {plant.name: plant.height for plant in plants}

    total_days = 7
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for _ in range(1, total_days):
        for plant in plants:
            plant.grow()
            plant.age()

    print(f"=== Day {total_days} ===")
    for plant in plants:
        print(plant.get_info())

    print("\nGrowth this week:")
    for plant in plants:
        growth = plant.height - initial_heights[plant.name]
        print(f"{plant.name}: +{growth}cm")
