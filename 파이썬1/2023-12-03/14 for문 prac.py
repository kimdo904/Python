# 1. 1부터 5 사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램을 구현하시오.

# 실행 예) 5,4,3,2,1

for i in range(5,0,-1):
    print(i, end=",")

# 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤
# 1부터 입력받은 정수까지 모든 정수의 합계를 출력하는 프로그램을 작성하시오.

# 실행 예)
# 임의의 양수를 입력하세요 >>> 5
# 1부터 5까지의 모든 정수의 합계는 15입니다.

# num = int(input("임의의 양수를 입력하세요 >>>"))
# sum = 0
# for i in range(1,num+1):
#     sum += i
# print(f'1부터 {num}까지의 모든 정수의 합계는 {sum}입니다.')

# 3. 사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일이름'을 입력받아 'baskey'리스트에 저장하는 프로그램을 구현하시오.
num = int(input("몇 개의 과일을 보관할까요?"))
baskey = []
for i in range(1, num+1):
    a = input(f'{i}번째 과일을 입력하세요 >>')
    baskey.append(a)
print(baskey)