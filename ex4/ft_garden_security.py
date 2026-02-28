class SecurePlant:
    """Blueprint for a secure garden plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant and call setters for validation."""
        self.name = name
        self._height: int | None = None
        self._age: int | None = None
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set plant height with validation."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            action = "initialized" if self._height is None else "updated"
            self._height = height
            print(f"Height {action}: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set plant age with validation."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            action = "initialized" if self._age is None else "updated"
            self._age = age
            print(f"Age {action}: {age} days [OK]")

    def get_height(self) -> int | None:
        """Get the current plant height."""
        return self._height

    def get_age(self) -> int | None:
        """Get the current plant age."""
        return self._age

    def get_info(self) -> str:
        """Get plant information as formatted string."""
        height = self._height if self._height is not None else "N/A"
        age = self._age if self._age is not None else "N/A"
        return f"{self.name} ({height}cm, {age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.get_info()}")
