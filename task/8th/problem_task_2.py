class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


class Circle:
    def __init__(self, radius, x, y) -> None:
        self.radius = radius
        self.point = Point(x, y)

    def get_area(self) -> int:
        return (self.radius**2) * 3.14

    def get_center(self) -> Point:
        return self.point


def main():
    circle = Circle(4, 3, 5)
    print(circle.get_area())
    print(circle.get_center())


main()
