# 임의의 두 자리 정수(10~99)를 입력받아서 십의 자리와 일의자리로 분리하여 출력하는 프로그램을 구현하시오.
num = int(input("두 자리 정수(10~99)를 입력하세요."))
num_10 = num // 10
num_1 = num % 10
print(f'{num}의 십의 자리 수는 {num_10}이고 일의 자리 수는 {num_1}이다.')
