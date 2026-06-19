import random


class Dice:
    def __init__(self) -> None:
        self.face = 0

    def roll(self) -> int:
        self.face = random.randint(1, 6)
        return self.face


def main():
    dice = Dice()
    print(dice.roll())


main()
