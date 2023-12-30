# 다음은 break문을 사용하여 사용자로부터 숫자를 입력받고 입력된 숫자가 10보다 크면 반복문이 종료되고 10보다 작으면 계속 반복되는 코드를 만들어 보시오.
num = int(input('숫자 입력 >>'))

while True:
    if num >= 10:
        break
    else:
        num = int(input('숫자 입력 >>'))