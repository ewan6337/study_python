from collections import namedtuple

Item = namedtuple("Item", ["name", "purchasePrice", "sellPrice"])

items = [
    Item("캔커피", 500, 1800),
    Item("삼각김밥", 900, 1400),
    Item("바나나우유", 800, 1800),
    Item("도시락", 3500, 4000),
    Item("콜라", 700, 1500),
    Item("새우깡", 1000, 2000)
]

totalPrice = 0

def mainScreen():
    print("1:구매 2:판매 3:현 매출 4:나가기")
    match int(input()):
        case 1:
            Purchase()
        case 2:
            Sell()
        case 3:
            print("현 매출은 %d원 입니다." %totalPrice)
            mainScreen()
        case 4:
            exit()

def SelectItem(classification_p_s: bool):
    index = 0
    match input("물건 이름을 입력해주세요.\n"):
        case "캔커피":
            index = 0
        case "삼각김밥":
            index = 1
        case "바나나우유":
            index = 2
        case "도시락":
            index = 3
        case "콜라":
            index = 4
        case "새우깡":
            index = 5
        case _:
            input("잘못 입력하셨습니다.")
            return PrintItemList(classification_p_s)
    return items[index]

def PrintItemList(classification_p_s: bool):
    price_attr = "purchasePrice" if classification_p_s == 0 else "sellPrice"
    for i in items:
        print("%s : %d원" % (i.name, getattr(i, price_attr)))
    action = "구매" if classification_p_s == 0 else "판매"
    print("어떤 것을 %s하시겠습니까?\n" % action)
    return SelectItem(classification_p_s)

def Purchase():
    global totalPrice
    item = PrintItemList(0)
    number = int(input("몇 개 구매하시겠습니까?\n"))
    print("%s을(를) %d개 구매합니다.\n매출 - %d" %(item.name, number, item.purchasePrice * number))
    totalPrice -= item.purchasePrice * number
    mainScreen()

def Sell():
    global totalPrice
    item = PrintItemList(1)
    number = int(input("몇 개 판매하시겠습니까?\n"))
    print("%s을(를) %d개 판매합니다.\n매출 + %d" %(item.name, number, item.sellPrice * number))
    totalPrice += item.sellPrice * number
    mainScreen()

mainScreen()
