fruits = ['사과','수박']
count = 3   # 입력 가능한 횟수

# 문제 1: count는 0이 되면 종료가 된다. 종료가 되고 나서는 '5개 과일은 . . . 입니다'가 출력이 되야 한다.
# 문제 2: 만약 동일한 과일이 입력될 경우, '동일한 과일이 있습니다'가 출력되고 count는 차감되지 않는다.
# 문제 3: 만약 다른 과일이 입력된 경우 count가 차감된다. 그리고 차감된 이후 '입력이 ...번 남았습니다.' 라는 문구가 떠야 한다.

# 방법1 : else 쓰면 continue 안써도 됨.
while count > 0:
    a = str(input("과일을 입력하세요 : "))
    if a in fruits:     # 리스트에 a가 있다면...
        print("이미 들어있는 과일입니다.")
        print(f'입력이 {count}번 남았습니다.')
        # continue    # while문의 시작점으로 돌아가서 다시 과일 이름 입력
    else:
        fruits.append(a)
        count -= 1
        print(f'입력이 {count}번 남았습니다.')
print(f'5개의 과일은 {fruits}입니다.')

# 방법2 : else 안쓰면 continue는 필수!
while count > 0:
    a = str(input("과일을 입력하세요 : "))
    if a in fruits:     # 리스트에 a가 있다면...
        print("이미 들어있는 과일입니다.")
        print(f'입력이 {count}번 남았습니다.')
        continue    # while문의 시작점으로 돌아가서 다시 과일 이름 입력
    fruits.append(a)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')
print(f'5개의 과일은 {fruits}입니다.')

