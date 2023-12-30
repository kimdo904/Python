# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력하는 프로그램을 구현하세요.
# 0 이하의 값이 입력되면 '잘못된 입력입니다.'라는 오류 메시지를 출력하세요.

# 실행 예)
# 정수를 입력하세요 >>> 2
# 1번째 Hello
# 2번째 Hello

num = int(input("정수를 입력하세요 >>>"))
if num >= 0:
    i = 1
    while i <= num:
        print(f'{i}번째 Hello')
        i = i+1
else:
    print("잘못된 입력입니다.")