def main():
    multiplicationTable(int (input("몇 단을 출력하시겠습니까?")))

def multiplicationTable(inputData : int):
    for i in range(1, 10, 1):
        print("%d * %d = %d" %(inputData, i, inputData * i))

main()