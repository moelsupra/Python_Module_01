"""Demonstrate inheritance by creating specialized plant types"""


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_data(self) -> str:
        """Return data of plant attributs"""
        cls_name = self.__class__.__name__
        return (f"{self.name} ({cls_name}): {self.height}cm, {self.age} days")


class Flower(Plant):
    """Represents a flowering plant that inherits from Plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with color attribute."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display a message about the flower blooming."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return super().get_data() + f", {self.color} color"


class Tree(Plant):
    """Represents a tree that inherits from Plant."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a tree with trunk diameter attribute."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and display the shade area produced by the tree"""
        shade_area = self.trunk_diameter * 1.5 + 3
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_info(self) -> str:
        return super().get_data() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Represents a Vegetable that inherits from Plant."""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """Initialize a vegetable with harvest info."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition_info(self) -> None:
        """Display nutritional information about the vegetable."""
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def get_info(self) -> str:
        return super().get_data() + f", {self.harvest_season} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    # Create flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    # Create trees
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 60)

    # Create vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 60, "fall", "vitamin A")

    # Display flower info
    print(rose.get_info())
    rose.bloom()
    print()

    # Display tree info
    print(oak.get_info())
    oak.produce_shade()
    print()

    # Display vegetable info
    print(tomato.get_info())
    tomato.get_nutrition_info()
