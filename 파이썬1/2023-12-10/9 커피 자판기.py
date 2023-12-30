# 커피 자판기 프로그램.
# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 있는 커피의 종류와 가격
# '아메리카노' : 1000
# '카페라떼' : 1500
# '카푸치노' : 2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환
# 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환
# 5. 정상 주문이면 주문한 커피와 잔돈을 반환

def coffee_machine(money, coffe):
    print(f'{money}원에 {coffe}를 선택하셨습니다.')
    coffee_list = {
        '아메리카노': 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }

    if coffe not in coffee_list:    # 주문한 메뉴가 없는 경우
        print(f'{coffe}는 없는 메뉴입니다.')
        return money,"없는 메뉴"
    elif coffee_list[coffe] > money:    # 구매할 금액이 부족할 경우
        print(f"돈이 부족합니다.{coffe}는 {coffee_list[coffe]}원입니다.")
    else:       # 정상주문이면 잔돈과 선택한 커피를 반환
        return money-coffee_list[coffe],coffe

order = input("커피를 선택하세요(아메리카노, 카페라뗴, 카푸치노) >>>")
pay = int(input('얼마를 낼까요?'))

change, menu = coffee_machine(pay,order)
print(f'잔돈 : {change}원, 커피 : {menu}')


