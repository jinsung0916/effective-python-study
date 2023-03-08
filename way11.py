# BETTER WAY 11 시퀀스를 슬라이싱하는 방법을 익혀라

a = ['a', 'b', 'c', 'd', 'e' ,'f', 'g', 'h']
print('가운데 2개', a[3:5])
print('마지막을 제외한 나머지', a[1:7])

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

first_twenty_items = a[20:]
last_twenty_items = a[-20:]

b = a[3:]
print('이전:', b)
b[1]= 9
print('이후:', b)
print('변화 없음:', a)

print('이전:', a)
a[2:7] = [99, 22, 14]
print('이후', a)

print('이전:', a)
a[2:3] = [47, 11]
print('이후', a)

b = a[:]
assert b == a and b is not a

b = a
print('이전 a:', a)
print('이전 b:', b)
a[:] = [101, 102, 103]
assert a is b
print('이후 a:', a)
print('이후 b:', b)
