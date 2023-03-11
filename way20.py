# BETTER WAY 20 None을 반환하기보다는 예외를 발생시켜라

def careful_devide(a: float, b: float) -> float:
    """a를 b로 나눈다.

    Raise:
        ValueError: b가 0이어서 나눗셈을 할 수 없을 때
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError

x, y = 5, 2
try:
    result = careful_devide(x, y)
except ValueError:
    print('잘못된 입력')
else:
    print(f'결과는 {result} 입니다.')