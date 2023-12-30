# 구구단 2단부터 9단까지 출력
# 각 단 앞에 제목, 마지마게 구분선을 넣어볼 것

dan = 2

while dan<=9:
    i = 1
    print(f'{dan}단')
    while i <= 9:
        print(f'{dan} x {i} = {dan*i}')
        i += 1
    print('-------------------')
    dan += 1
