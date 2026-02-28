class Plant:
    """Base class representing a regular plant."""
    plant_type = "regular"

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return basic plant information."""
        return f"{self.name}: {self.height}cm"

    def get_score_value(self) -> int:
        """Return plant contribution to garden score."""
        return self.height

    def validate_height(height: int) -> bool:
        """Validate that height is non-negative."""
        return height >= 0
    validate_height = staticmethod(validate_height)


class FloweringPlant(Plant):
    """Plant subclass that produces flowers."""
    plant_type = "flower"

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        is_blooming: bool
    ) -> None:
        """Initialize flowering plant with additional flower data."""
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def get_info(self) -> str:
        """Return flowering plant information."""
        bloom = "blooming" if self.is_blooming else "not blooming"
        return super().get_info() + f", {self.color} flowers ({bloom})"


class PrizeFlower(FloweringPlant):
    """Special flowering plant that has prize points."""
    plant_type = "prize"

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        is_blooming: bool,
        prize: int
    ) -> None:
        """Initialize prize flower with additional prize points."""
        super().__init__(name, height, age, color, is_blooming)
        self.prize = prize

    def get_info(self) -> str:
        """Return prize flower information."""
        return super().get_info() + f", Prize points: {self.prize}"

    def get_score_value(self) -> int:
        """Override score calculation to include prize points."""
        return self.height + self.prize


class GardenManager:
    """Manager class responsible for handling gardens and analytics."""
    total_gardens = 0

    class GardenStats:
        """Nested helper class used for garden statistics."""

        def calculate_total_height(plants: list) -> int:
            """Calculate total height of all plants."""
            total = 0
            for plant in plants:
                total += plant.height
            return total
        calculate_total_height = staticmethod(calculate_total_height)

        def count_flowering_plants(plants: list) -> int:
            """Count flowering plants."""
            count = 0
            for plant in plants:
                if plant.plant_type == "flower":
                    count += 1
            return count
        count_flowering_plants = staticmethod(count_flowering_plants)

        def count_prize_flowers(plants: list) -> int:
            """Count prize flowers."""
            count = 0
            for plant in plants:
                if plant.plant_type == "prize":
                    count += 1
            return count
        count_prize_flowers = staticmethod(count_prize_flowers)

    def __init__(self, owner_name: str) -> None:
        """Initialize garden with owner name and empty plant list."""
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add plant to garden after validating height."""
        if Plant.validate_height(plant.height):
            self.plants += [plant]
            print(f"Added {plant.name} to {self.owner_name}'s garden")
        else:
            print("Invalid height")

    def help_all_plants_grow(self) -> None:
        """Increase height of all plants by 1cm."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def get_report(self) -> None:
        """Display detailed garden report."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")

        total_plants = 0
        for plant in self.plants:
            print(f"- {plant.get_info()}")
            total_plants += 1

        flowering_count = GardenManager.GardenStats.count_flowering_plants(self.plants)
        prize_count = GardenManager.GardenStats.count_prize_flowers(self.plants)
        regular_count = total_plants - flowering_count - prize_count

        print(
            f"\nPlants added: {total_plants}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            f"Plant types: {regular_count} regular, "
            f"{flowering_count} flowering, {prize_count} prize flowers"
        )

    def calculate_score(self) -> int:
        """Dynamically calculate garden score using polymorphism."""
        total = 0
        for plant in self.plants:
            total += plant.get_score_value()
        return total

    def create_garden_network(cls, owner_names: list) -> list:
        """Class method that creates multiple gardens."""
        gardens = []
        for name in owner_names:
            gardens += [cls(name)]
        return gardens
    create_garden_network = classmethod(create_garden_network)

    def get_total_gardens(cls) -> int:
        """Return total number of gardens created."""
        return cls.total_gardens
    get_total_gardens = classmethod(get_total_gardens)


def compare_garden_scores(g1: GardenManager, g2: GardenManager) -> None:
    """Non-member function comparing two gardens."""
    print(
        f"Garden scores - {g1.owner_name}: {g1.calculate_score()}, "
        f"{g2.owner_name}: {g2.calculate_score()}"
    )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice, bob = GardenManager.create_garden_network(["Alice", "Bob"])

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", True, 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print()
    alice.help_all_plants_grow()

    print()
    alice.get_report()

    print()
    print(f"Height validation test: {Plant.validate_height(rose.height)}")

    pine = Plant("Pine", 80, 500)
    bob.add_plant(pine)

    print()
    compare_garden_scores(alice, bob)

    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")