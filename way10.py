# BETTER WAY 10 대입식을 사용해 반복을 피하라

fresh_fruits = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5
}

def make_lemonade(count):
    ...

def out_of_stock():
    ...

if count := fresh_fruits.get('레몬', 0):
    make_lemonade(count)
else:
    out_of_stock()

def slice_bananas(count):
    ...

class OutOfbananas(Exception):
    pass

def make_smoothis(count):
    ...

if (count := fresh_fruits.get('바나나', 0)) > 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothis(pieces)
except OutOfbananas:
    out_of_stock()

def make_cider(count):
    ...

if(count := fresh_fruits.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothis(pieces)
elif(count := fresh_fruits.get('사과', 0)) >= 2:
    to_enjoy = make_cider(count)
elif(count := fresh_fruits.get('레몬', 0)):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = '아무것도 없음'

def pick_fruit():
    ...

def make_juice(fruit, count):
    ...

bottle = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottle.extend(batch)