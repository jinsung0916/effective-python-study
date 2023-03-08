# BETTER WAY 15 딕셔너리 삽입 순서에 의존할 때는 조심하라

baby_names = {
    'cat': 'kitten',
    'dog': 'puppy'
}

print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(list(baby_names.popitem()))

def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_func(goose='gosling', kangaroo='joey')

class MyClass:
    def __init__(self) -> None:
        self.alligator = 'hatchling'
        self.elephant = 'calf'
    
a = MyClass()
for key, value in a.__dict__.items():
    print(f'{key} = {value}')