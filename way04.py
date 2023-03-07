# BETTER WAY 4 C 스타일 형식 문자열을 str.format과 쓰기보다는 f-문자열을 통한 인터폴레이션을 사용하라

key = "my_var"
value = 1.234

formatted = f"{key} = {value}"
print(formatted)

formatted = f"{key!r:<10} = {value:.2f}"
print(formatted)

pentry = [
    ('apple', 1),
    ('banana', 2),
    ('cinamon', 3),
]

for i, (item, count) in enumerate(pentry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item,
        round(count)
    )

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item,
        round(count)
    )

    f_string = f'#{i+1}: {item:<10s} = {count}'

assert old_style == new_style == f_string


places = 2
number = 1.234
print(f'내가 고른 숫자는 {number:.{places}f}')