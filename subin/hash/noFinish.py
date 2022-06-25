def solution(participant, completion):
    answer = set(participant) - set(completion)
    answer = "".join(answer)
    return answer

#print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# set 함수를 이용할 경우 중복을 허용하지 않기 때문에 동명이인에 대해 처리를 못함 

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
