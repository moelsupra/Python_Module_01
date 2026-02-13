class Plant():
    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self):
        self.height += 1

    def age(self):
        self.ages += 1
    
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.ages} days old"

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    for day in range(6):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +6cm")