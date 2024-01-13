# 동료 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt' 파일을 읽어서
# '꿀' 이라는 글자가 몇 번 나오는지 찾는 프로그램입니다.

# hint : 문자 자체를 받으려면 문자열을 먼저 추출 후 문자를 추출하는 형식이여야 한다.

file = open('엄마돼지아기돼지.txt', 'rt')

line_list = file.readlines()
print(line_list)

count = 0
for line in line_list:
    for str in line:
        if str == '꿀':
            count += 1

print(f'"꿀"는 {count}번 나왔습니다.')