# 1부터 100사이의 모든 정수 중에서 7의 배수만 출력하는 프로그램을 구현하세요.
num =1
while num<=100:
    if(num % 7 ==0):
        print(num)
    num += 1

# 강사님 풀이
n = 7
while n <= 100:
    print(n)
    n += 7