class Rectangle:
    def __init__(self, x, y, w, h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, w = {self.w}, h = {self.h}"

    def get_area(self) -> int:
        return self.w * self.h

    def overlap(self, r: "Rectangle") -> bool:
        if (
            r.x - (r.w / 2) > self.x + (self.w / 2)
            or r.x + (r.w / 2) < self.x - (self.w / 2)
            or r.y - (r.h / 2) > self.y + (self.h / 2)
            or r.y + (r.h / 2) < self.y - (self.h / 2)
        ):
            print(f"{self}와 {r}은 서로 겹치지 않습니다.")
            return False
        else:
            print(f"{self}와 {r}은 서로 겹칩니다.")
            return True


def main():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    r1.overlap(r2)


main()
