# continue 문
# 반복문의 시작 지점으로 제어의 흐름을 옮기는 역할
# 반복에서 제외하거나 생략하고 싶은 코드가 존재할 때 사용

# 1부터 100 사이의 모든 정수를 합하는데 3의 배수만 제외
total = 0
for i in range(1,101):
    if i % 3 == 0:  # 3의 배수인지 확인
        continue
    total += i
print(f'1부터 100까지 3의 배수를 제외한 모든 수의 합은 {total}')

# continue를 사용하지 않고 3의 배수는 제외해서 문제를 풀어보시오.
total = 0
for i in range(1,101):
    if i % 3 == 0:
        total += 0
    else:
        total += i
print(total)