# 개인정보의 보안 처리를 위하여 주어진 인수의 일부를 *로 바꾸어 반환하는 함수를 만들어서
# 이를 모듈로 저장하는 프로그램입니다.

# 모듈명 : mysecure.py -> 여기서 실행되어야 함
# secure_name() 함수 : 김철수 -> 김**
# secure_no() 함수 : 991216-1234567 -> 991216-1******
# secure_phone() 함수 : 010-1234-5678 -> 010-****-5678

def secure_name(data):
    return data[:1] + '*' * (len(data)-1)

def secure_no(data):
    return data[:8] + '*' * (len(data)-8)
    # return data[0:8] + '******'

def secure_phone(data):
    return data[:4] + '*' * (len(data)-9) + data[8:]
    # return data.replace(data[4:8], '****')