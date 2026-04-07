won = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

inputPriseWon = int(input("교환할 돈을 입력하시오:"))

for i in won:
    if inputPriseWon // i != 0:
        print("%d원권 %d장" %(i, inputPriseWon // i))
        inputPriseWon %= i