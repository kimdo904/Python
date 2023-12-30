# 1.
money = 9000

# 나이를 입력받아 19세 이상이면 1250원, 13 ~ 18 : 1050원, 7 ~ 12 : 650원, 7세 미만 : 0원
# 잔액은 ... 입니다.

# age = int(input("나이를 입력하세요 >>"))
# fee1 = 1250
# fee2 = 1050
# fee3 = 650
# fee4 = 0
# if age>19:
#     print(f'금액은 {fee1}원입니다.잔액은 {money - fee1}입니다.')
# elif age>12:
#     print(f'금액은 {fee2}원입니다.잔액은 {money - fee2}입니다.')
# elif age>6:
#     print(f'금액은 {fee3}원입니다.잔액은 {money - fee3}입니다.')
# else:
#     print(f'금액은 {fee4}원입니다.잔액은 {money - fee4}입니다.')

# 2. 사용자로부터 하나의 정수를 입력받고 정수가 홀수인지 짝수인지 판별하여 출력

# num = int(input("정수를 입력하세요 >>>"))
# if num % 2 == 0:
#     print(f'{num}은 짝수입니다.')
# else:
#     print(f'{num}은 홀수입니다.')

# 3. 사용자로부터 정수를 입력받아 해당 정수의 구구단을 출력하는 프로그램을 작성하세요.
# num = int(input('몇 단을 출력할까요?(2~9) >>>'))
# print(f'{num}단')
# for i in range(1, 10):
#     print(f'{num} x {i} = {num*i}')

# 4. 사용자로부터 여러 개의 정수를 입력받아 입력된 숫자 중에서 가장 큰 값을 찾아 출력하는 프로그램을 작성하세요. 숫자입력은 무한대로 받을 수 있다. 단 -1을 입력하는 순간 종료되며 큰 값을 출력하게 된다.
max_num = None
while True:
    num = int(input('정수 입력(-1 입력시 종료) >>>'))
    # 입력값이 -1인 경우 루프 종료
    if num == -1:
        print('프로그램 종료')
        break
    # 최대값 업데이트
    if max_num is None or num > max_num:
        max_num = num

# 최대값 출력
if max_num is not None:
    print(f'입력된 숫자 중에서 가장 큰 값은 {max_num}입니다.')
else:
    print('입력된 숫자가 없습니다.')

# 5. 사용자로부터 하나의 정수를 입력받아 해당 숫자만큼 높이를 가진 삼각형 모양의 별을 출력하는 프로그램을 작성하시오. 예를 들어 입력이 5라면 다음과 같이 출력한다.

# *
# **
# ***
# ****
# *****
#
# num = int(input('몇 층까지 찍을까요?'))
# for i in range(1, num+1):
#     print('*' * i)