# BETTER WAY 21 변수 영역과 클로저의 상호작용 방식을 이해하라

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

def sort_priority2(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        else:
            return (1, x)
    values.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
found = sort_priority2(numbers, group)
print(numbers, found)