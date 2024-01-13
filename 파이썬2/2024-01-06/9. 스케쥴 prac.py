# 오늘의 스케쥴을 입력하면 그 내용이 모두 파일에 보관되는 프로그램이다.
# 스케쥴을 입력하지 않고 enter 누르면 프로그램을 종료됩니다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2024-01-06.txt'와 같은 형식을 갖추고 있습니다.
# hint : time 모듈을 불러오시오. # time.strftime 을 검색해보고 사용하시오.

from time import *
def save_schedule():

    current_date = strftime("%Y-%m-%d")
    # file = open('./output/current_date.txt', 'wt', encoding='utf-8')
    file_name = f'./output/{current_date}.txt'
    print("아무것도 없게 될 시 (아무것도 없는 상태에서 enter을 입력시 종료)")
    schedules = []
    while(True):
        schedule = input("오늘의 스케쥴 입력>>")
        schedules.append(schedule)
        # print("아무것도 없게 될 시 (아무것도 없는 상태에서 enter을 입력시 종료)")
        if not schedule:
            print('프로그램 종료')
            break


    file = open(file_name, 'wt', encoding='utf-8')
    file.write('\n'.join(schedules))

    print(f'스케줄이 {file_name} 파일에 저장되었습니다.')

save_schedule()