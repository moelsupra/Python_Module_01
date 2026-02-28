class Plant:
    """
    Represents a plant in the garden
    Attributes: name, height, age of the plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant Args : Name ..."""
        self.name = name
        self.height = height
        self.age = age

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
