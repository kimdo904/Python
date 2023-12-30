# 출력하고자 하는 구구단을 입력받아 구구단을 출력(단 while문 사용금지)

# 실행 예 : 출력할 구구단을 입력하세요 >> ex) 5단 -> 5단만 출력

dan = int(input("출력할 구구단을 입력하세요 >>"))
for i in range(1,10):
    print(f'{dan} x {i} = {dan * i}')


