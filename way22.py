# BETTER WAY 22 변수 위치 인자를 사용해 시각적인 잡음을 줄여라

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는 ', 1, 2)

favorites = [1, 2, 3]
log('좋아하는 숫자는', *favorites)

def my_generator():
    for x in range(10):
        yield x

def my_func(*args):
    print(args)

it = my_generator() 
my_func(*it) # 제너레이터의 모든 원소를 얻기 위해 반복함