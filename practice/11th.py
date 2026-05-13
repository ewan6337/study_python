def main():
    loop:
        input_vlaue = input(계산할 반지름을 입력하세요:)
        if (input_value == q):
            exit
        else:
            tmp_Circle = Circle(input_vlaue)
            print("원의 넓이는 %d입니다" %tmp_Circle.calculate_aria())
            print("원의 둘레는 %d입니다" %calculate_perimeter())

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius

    def calculate_aria(self):
        return math.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * math.pi * radius

main()
