# BETTER WAY 12 스트라이드와 슬라이스를 한 식에 함께 사용하지 말라

x = ['빨강', '주황', '노랑', '초록', '파랑', '자주']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = b'mongoose'
y = x[::-1]
print(y)

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = x[::2]
z = y[1:-1]
print(z)