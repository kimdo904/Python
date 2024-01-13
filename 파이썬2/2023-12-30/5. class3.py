# 딕셔너리를 리턴하는 함수를 선언. 반복되는 키 입력을 줄임.

def create_student(name,korean,math,english,science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
# 학생 리스트를 선언
students = [
    create_student("연하진", 92,98,96,98),
    create_student("구지연", 96, 98, 93, 94),
    create_student("나선주", 92, 94, 94, 96),
    create_student("윤아린", 93, 92, 95, 97),
    create_student("윤명월", 94, 91, 99, 98),
]

# 학생을 한명씩 반복
print("이름", "    총점",  "평균", sep = "\t\t")
for student in students:
    # 점수의 총합과 평균을 구함.
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep = "\t\t")


