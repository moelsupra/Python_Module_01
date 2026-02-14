""""use data validation and encapsulation to protect plant data integrity"""


class SecurePlant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set plant height with validation"""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set plant height with validation"""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Get the current plant height"""
        return self._height

    def get_age(self) -> int:
        """Get the current plant age"""
        return self._age

    def get_info(self) -> str:
        """Get plant informations as formatted string"""
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created: Rose")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.get_info()}")
