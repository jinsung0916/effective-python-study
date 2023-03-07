# BETTER WAY 5 복잡한 식을 쓰는 대신 도우미 합수를 작성하라

from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=3&초록=', keep_blank_values=True)
print(repr(my_values))

def get_first_int(values, key, default=0):
    found = values.get(key, [''])[0]
    if found:
        return int(found)
    else: 
        return default

print(get_first_int(my_values, '빨강'))
print(get_first_int(my_values, '파랑'))
print(get_first_int(my_values, '초록'))