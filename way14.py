# BETTER WAY 14 복잡한 기준을 사용해 정렬할 때는 key 파라미터를 사용하라

numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

class Tool:
    def __init__(self, name, weight):
        self.name = name 
        self.weight = weight
    
    def __repr__(self):
        return f'Tool({self.name},  {self.weight})'
    
tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', 0.5),
    Tool('골', 0.25)
]

tools.sort(key=lambda x: x.name)
print(tools)

tools.sort(key=lambda x: x.weight)
print(tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print(places)
places.sort(key= lambda x: x.lower())
print(places)

power_tools = [
    Tool('드릴', 4),
    Tool('원형 톱', 5),
    Tool('착암기', 40),
    Tool('연마기', 4) 
]

power_tools.sort(key=lambda x: (x.name, x.weight))
print(power_tools)

power_tools.sort(key=lambda x: (x.name, x.weight), reverse=True)
print(power_tools)

power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)

# 리스트에서 얻어내고 싶은 정렬 기준 우선순위의 역순
power_tools.sort(key=lambda x: x.name)
power_tools.sort(key=lambda x: x.weight, reverse=True)
print(power_tools)