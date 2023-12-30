
# Watch 클래스 선언
class Watch():
    # 생성자 선언
    # def __init__(self, hour=0, minute=0, second=0):
    #     self.hour = hour
    #     self.minute = minute
    #     self.second = second
        # self.time = {"hour": self.hour, "minute": self.minute, "second": self.second}
    # What 메서드 생성
    def What(self):
        time = input('시간 입력 >>')
        time_list = time.split(':')
        self.hour = int(time_list[0])
        self.minute = int(time_list[1])
        self.second = int(time_list[2])
    # def What(self):
    #     self.time["hour"] = int(input("시각을 입력 >>"))
    #     self.time["minute"] = int(input("분을 입력 >>"))
    #     self.time["second"] = int(input("초를 입력 >>"))
    #     return self.time
    # see 메서드 생성
    def see(self):
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다.')
    # def see(self):
    #     print(f'계산된 시간은 {self.time["hour"]}시 {self.time["minute"]}분 {self.time["second"]}초입니다')

watch = Watch()
watch.What()
watch.see()

