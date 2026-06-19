class Person:
    def __init__(self, name, id, age, height, weight):
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Person Class's {self.name}"


def main():
    person_list = [
        Person("을지문덕", 0, 1, 178, 94),
        Person("계백", 1, 1, 166, 78),
        Person("김유신", 2, 1, 184, 102),
        Person("강감찬", 3, 1, 170, 80),
        Person("이순신", 4, 1, 169, 72),
    ]

    for i in person_list:
        print(
            i, f"name: {i.name}, age: {i.age}, height: {i.height}, weight: {i.weight}"
        )


main()
