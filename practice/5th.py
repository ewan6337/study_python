def main():
    multiplication(int(input("곱셈을 출력할 단을 입력하세요:")))

def multiplication(inputData: int):
    for i in range(1, 10, 1):
        print("%d * %d = %d" %(inputData, i, inputData * i))

main()