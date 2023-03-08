# BETTER WAY 13 슬라이싱보다는 나머지를 모두 잡아내는 언패킹을 사용하라

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, others, youngest)

short_list = [1, 2]
first, second, *others = short_list
print(first, second, others)

def generate_csv():
    yield ('날짜', '제조사', '모델', '연식', '가격')

header, *rows = generate_csv()
print('CSV 헤더:', header)
print('행 수:', len(rows))

