list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    triple = lambda a: a**3
    for i in range(10):
        print(triple(list[i]))


main()
