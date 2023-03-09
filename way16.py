# BETTER WAY 16 in을 사용하고 딕셔너리 키가 없을 때 KeyError를 처리하기보다 get을 사용하라

counter = {
    '품퍼니켈': 2,
    '사워도우': 1
}

key = ''
count = counter.get(key, 0)
counter[key] = count + 1


votes = {
    '바게트': ['철수', '순이'],
    '치아바타': ['하니', '유리']
}

key = '브리오슈'
who = '단어'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

if(names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)
print(votes)