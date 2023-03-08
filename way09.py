# BETTER WAY 9 for이나 while 루프 뒤에 else 블록을 사용하지 말라

for i in range(3):
    print('Loop', i)
else:
    print('Else block!')

for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block!')

for x in []:
    print('이 줄은 실행되지 않음')
else:
    print('For Else block!')

a = 4
b = 9

# 이렇게 사용하지 말것!
for i in range(min(a, b), 1):
    print('검사중', i)
    if a % i == 0 and b % i == 0:
        print('서로소 아님')
        break
else:
    print('서로소')

# 도우미 함수를 이용하자
def coprime(a, b):
    for i in range(min(a, b), 1): 
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4, 9)