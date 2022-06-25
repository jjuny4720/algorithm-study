from functools import reduce

def solution(clothes):
    d = {}

    for i in clothes:
        #print(i[1])
        if i[1] not in d.keys():
            d[i[1]] = 1
        else:
            d[i[1]] += 1
    
    #print(d) # {'headgear': 2, 'eyewear': 1}
    
    for i in d:
        d[i] += 1

    answer = list(d.values())
    
    return reduce(lambda x, y: x * y, answer) - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))