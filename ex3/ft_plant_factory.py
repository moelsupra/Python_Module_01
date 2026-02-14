"""Demonstrate efficient plant creation using the Plant class constructor"""


class Plant():
    """Represents a plant that can be created with initial values"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")

    total: int = 0
    for plant in plants:
        print(f"Created: {plant.get_info()}")
        total += 1

    print(f"\nTotal plants created: {total}")
