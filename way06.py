# BETTER WAY 6 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라

snack_calories = {
    '감자칩': 140,
    '팝콘': 80,
    '땅콩': 190
}

item = tuple(snack_calories.items())
print(item)

item = ('호박엿', '식혜')
first = item[0]
second = item[1]
print(first, '&', second)

item = ('호박엿', '식혜')
(first, second) = item
print(first, '&', second)

favorite_snacks = {
    '짭조름한 과자': ('프레즐', 100),
    '달콤한 과자': ('쿠키', 180),
    '채소': ('당근', 20)
}

((type1, (name1, cal1)),
 (type2, (name2, cal2)),
 (type3, (name3, cal3))) = favorite_snacks.items()

print(f'제일 좋아하는 {type1} 는 {name1}, {cal1} 입니다.')
print(f'제일 좋아하는 {type2} 는 {name2}, {cal2} 입니다.')
print(f'제일 좋아하는 {type3} 는 {name3}, {cal3} 입니다.')

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if(a[i-1] > a[i]):
                a[i-1], a[i] = a[i], a[i-1]

names = ['프레즐', '당근', '쑥갓', '베이컨']
bubble_sort(names)
print(names)

snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]

for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} 은 {calories} 칼로리입니다.')