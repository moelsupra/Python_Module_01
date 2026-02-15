class GardenManager:
    """Manages multiple gardens and provides analytics"""
    total_gardens: int = 0

    class GardenStats:
        """Nested helper class for calculating garden statistics."""
        @staticmethod
        def calculate_total_height(plants) -> int:
            """Calulate total height of all plants"""
            total: int = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def count_flowering_plants(plants) -> int:
            """Count flowering plants"""
            count: int = 0
            for plant in plants:
                if plant.plant_type == "flower":
                    count += 1
            return count

        @staticmethod
        def count_prize_flower(plants) -> int:
            """Count prize flowers"""
            count: int = 0
            for plant in plants:
                if plant.plant_type == "prize":
                    count += 1
            return count

    def __init__(self, owner_name: str) -> None:
        """Initialize a new garden manager"""
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        """Add plant to the garden"""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_all_plant_grow(self) -> None:
        """Make all plants grow by 1cm"""
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def get_report(self) -> None:
        """Display reprot of the garden"""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")

        flowering_count = self.GardenStats.count_flowering_plants(self.plants)
        prize_count = self.GardenStats.count_prize_flower(self.plants)
        total_plants = len(self.plants)

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
        """Calculate garden score based on total plant height"""
        return self.GardenStats.calculate_total_height(self.plants)

    @classmethod
    def create_garden_network(cls, owner_names) -> list:
        """Create multiple gardens at once"""
        gardens = []
        for name in owner_names:
            gardens.append(cls(name))
        return gardens

    @classmethod
    def get_total_gardens(cls) -> int:
        """Get total number of gardens created"""
        return cls.total_gardens


class Plant:
    """Class representing regular plant"""
    plant_type = "regular"

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Get plant information"""
        return f"{self.name}: {self.height}cm"

    @staticmethod
    def validate_height(height: int) -> bool:
        """validate if height is acceptable"""
        return height >= 0


class FloweringPlant(Plant):
    """class inherit from plant representing flower"""
    plant_type = "flower"

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        is_blooming: bool
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def get_info(self) -> str:
        """Get plant information"""
        blom = "blooming" if self.is_blooming else "not blooming"
        return super().get_info() + f", {self.color} flowers ({blom})"


class PrizeFlower(FloweringPlant):
    """class inherit from FloweringPlant representing a prize-winning flower"""
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
        super().__init__(name, height, age, color, is_blooming)
        self.prize = prize

    def get_info(self) -> str:
        """Get plant information"""
        return super().get_info() + f", Prize points: {self.prize}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", True, 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.help_all_plant_grow()
    print()
    alice.get_report()

    print()
    print(f"Height validation test: {Plant.validate_height(rose.height)}")

    print()
    bob = GardenManager("Bob")
    pine = Plant("Pine", 80, 500)
    bob.plants.append(pine)

    print(
        f"Garden scores - Alice: {alice.calculate_score()}, "
        f"Bob: {bob.calculate_score()}"
    )
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
