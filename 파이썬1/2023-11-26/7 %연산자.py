# % 연산자
name = 'KoreaIT'
print('나의 학원은 %s입니다' %name) # %s : string(문자열)
print('나의 학원은 ', name, '입니다', sep='')
print('나의 학원은 '+ name + '입니다')  # best choice

height = 120.5
print('내 키는 %.1fcm입니다.' % height)   # %f : float(실수형)

weight = 23.55
print('내 몸무게는 %.1fkg입니다.' %weight)

year, month, day = 2023, 11, 26
print('오늘은 %d년 %d월 %d일입니다.' % (year, month, day))
# %d : 정수형(int) decimal(십진법)

