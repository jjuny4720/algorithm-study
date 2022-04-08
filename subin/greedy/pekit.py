def solution(n, lost, reserve):
    
    reserve.sort()
    
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    for j in reserve:
        if j in lost:
            lost.remove(j)
        elif j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
            
    answer = n - len(lost)
    print(answer)
    return answer

n = 5
lost = [2,4]
reserve = [3,1]

solution(n, lost, reserve)