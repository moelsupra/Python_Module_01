"""Create a Plant class to organize and display plant information"""


class Plant():
    """
    Represents a plant in the garden
    Attributes Name, Height, Age of plant
    """
    def __init__(self, name, height, age) -> None:
        """Initialize a new plant Args : Name ..."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def info(self) -> None:
        """Display plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.info()
    sunflower.info()
    cactus.info()
