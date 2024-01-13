# 학생 리스트를 선정. 딕셔너리 요소로 가진 리스트

# ctrl alt l : 자동 줄 맞춤
students = [
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 82, "math": 88, "english": 94, "science": 94},
    {"name": "나선주", "korean": 93, "math": 78, "english": 93, "science": 95},
    {"name": "윤아린", "korean": 94, "math": 98, "english": 92, "science": 96},
    {"name": "윤명월", "korean": 95, "math": 88, "english": 99, "science": 98}
]

# 학생을 한명씩 반복
print("이름", "    총점",  "평균", sep = "\t\t")
for student in students:
    # 점수의 총합과 평균을 구함.
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep = "\t\t")