# BETTER WAY 17 내부 상태에서 원소가 없는 경우를 처리할 때는 setdefault보다 defaultdict를 사용하라

visits = {
    '미국': {'뉴욕', '로스엔젤레스'},
    '일본': {'하코네'}
}

from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, key, value):
        self.data[key].add(value)

visits = Visits()
visits.add('영국', '버스')
visits.add('영국', '런던')
print(visits.data)