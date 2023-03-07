# BETTER WAY 7 range보다는 enumerate를 사용하라

from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))

flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛있어요.')

for i in range(len(flavor_list)):
    print(f'{i+1}: {flavor_list[i]}')

it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flaver in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')

for i, flaver in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')