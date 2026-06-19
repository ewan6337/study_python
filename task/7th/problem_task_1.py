def calculate_stocked_fruits_in_home(fruits):
    totalMoney = 0
    for product, value in fruits.items():
        price, number = value
        if number >= 5:
            print("%s is not needed to buy" %product)
        else:
            print("%s is needed to buy" %product)
            neededMoney = price * (5 - number)
            totalMoney = totalMoney + neededMoney
            print("  To buy it: pay:%d Won" %neededMoney)
    return totalMoney


if __name__ == '__main__':
    fruits = {
        "pear":         [2000, 3],
        "apple":        [1500, 5],
        "strawberry":   [1800, 2],
        "melon":        [2300, 5]
    }

    totalMoney = calculate_stocked_fruits_in_home(fruits)
    print ("\nTotal money:", totalMoney)
