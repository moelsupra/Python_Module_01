"""Simulate plant growth over time with methods to modify plant state."""


class Plant():
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
    # Create individual plants first
    rose = Plant("Rose", 25, 30)
    tulip = Plant("Tulip", 15, 10)
    sunflower = Plant("Sunflower", 40, 20)

    # Store plants in a list
    plants = [rose, tulip, sunflower]

    # Save initial heights in a dictionary
    initial_heights = {plant.name: plant.height for plant in plants}

    total_days = 7
    # Day 1
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    # Simulate the rest of the week (6 more days)
    for _ in range(total_days - 1):
        for plant in plants:
            plant.grow()
            plant.age()

    # Day 7
    print(f"=== Day {total_days} ===")
    for plant in plants:
        print(plant.get_info())

    # Show growth
    print("\nGrowth this week:")
    for plant in plants:
        growth = plant.height - initial_heights[plant.name]
        print(f"{plant.name}: +{growth}cm")










if __name__ == "__maiffn__":
    rose = Plant("Rose", 25, 30)
    growth_start = rose.height
    initial_age = rose.age
    print(f"=== Day {rose.age - initial_age + 1} ===")
    print(rose.get_info())
    for day in range(6):
        rose.grow()
        rose.add_one_day_in_age()
    growth_end = rose.height

    print(f"=== Day {rose.age - initial_age + 1} ===")
    print(rose.get_info())
    print(f"Growth this week: +{growth_end - growth_start}cm")
