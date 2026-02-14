"""Simulate plant growth over time with methods to modify plant state."""


class Plant():
    """Represent a plant that can grow and age over time"""
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        """Increase plant height by 1cm"""
        self.height += 1

    def add_one_day_in_age(self) -> None:
        """Increase plant age by 1 day"""
        self.age += 1

    def get_info(self) -> str:
        """Get plant information as a formatted string"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    growth_start = rose.height
    print("=== Day 1 ===")
    print(rose.get_info())
    for day in range(6):
        rose.grow()
        rose.add_one_day_in_age()
    growth_end = rose.height
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{growth_end - growth_start}cm")
