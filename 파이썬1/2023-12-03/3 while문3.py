# 사용자로부터 임의의 정수를 입력받아 모두 리스트에 보관
# 단 사용자가 0을 입력하면 프로그램을 종료, 이때 입력받은 0은 리스트에 보관하지 않음


list = []
run = True
while (run):
    num = int(input("정수를 입력하세요>>>"))
    if (num == 0):
        run = False
        print("프로그램 종료")
    else:
        list.append(num)
    print(list)

# 문제 접근 방법 : 빈 리스트 생성, 정수를 입력, while문(0이 아니면 계속 실행), 마지막에 찍어내면 끝
while   n!=0:
    list.append(n)
    n = int(input("정수를 입력하세요(종료는 0입니다.)"))

print(list)