import math

class Polygon:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def calculate_area(self):
        if self.num_sides < 3:
            return "A polygon must have at least 3 sides."
        
        n = self.num_sides
        s = self.side_length
        area = (n * s ** 2) / (4 * math.tan(math.pi / n))
        return round(area, 2)

    def display_info(self):
        print(f"\nPolygon with {self.num_sides} sides")
        print(f"Each side length: {self.side_length}")
        print(f"Area: {self.calculate_area()}")


num_sides = int(input("Enter the number of sides: "))
side_length = float(input("Enter the length of each side: "))

polygon = Polygon(num_sides, side_length)
polygon.display_info()

        