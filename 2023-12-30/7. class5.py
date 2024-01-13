class Myclass:
    # self : 특별한 예약어. 클래스의 인스턴스 메서드 안에서 사용된다.
    # 해당 메서드가 호출된 인스턴스를 가리킨다.
    # 생성자(__init__) : 클래스가 만들어질 때 무조건적으로 실행되는 함수
    def __init__(self, value):  # self는 Myclass를 가리킴.
        self.value = value
    def print_value(self):
        print(self.value)

obj = Myclass(42)

obj.print_value()



# 클래스를 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name    # 인스턴스 변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science    # 메서드

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f'{self.name}\t{self.get_sum()}\t\t{self.get_average()}'

students = [
    Student("연하진", 92,98,96,98),
    Student("구지연", 96, 98, 93, 94),
    Student("나선주", 92, 94, 94, 96),
    Student("윤아린", 93, 92, 95, 97),
    Student("윤명월", 94, 91, 99, 98),
]

# 학생을 한명씩 반복
print("이름", "총점",  "평균", sep = "\t\t")
for student in students:
    print(student.to_string())