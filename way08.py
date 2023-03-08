# BETTER WAY 8 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용해라

names = ['Cecilia', '남궁민수', 'AJ']
counts = [len(name) for name in names]
print(counts)

max_count = int()
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

names.append('Rosalind')

import itertools 

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')