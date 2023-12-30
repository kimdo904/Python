# 국어, 영어, 수학 점수를 각각 입력받아서 평균을 구하고, 평균이 80점 이상이면 '합격',
# 아니면 '불합격'을 출력하는 프로그램을 구현하세요.

# 실행 예)
# 국어 점수를 입력하세요 >>> 85
# 영어 점수를 입력하세요 >>> 83
# 수학 점수를 입력하세요 >>> 81

# 평균은 83.0이고, 결과는 합격입니다.

korea = int(input("국어 점수를 입력하세요 >>>"))
eng = int(input("영어 점수를 입력하세요 >>>"))
math = int(input("수학 점수를 입력하세요 >>>"))

avg = (korea+eng+math)/3
result = '합격' if avg>80 else '불합격'
print(f'평균은 {avg}이고, 결과는 {result}입니다.')