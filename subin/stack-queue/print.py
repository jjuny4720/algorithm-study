from collections import deque

def solution(priorities, location):
    temp = deque([i for i in range(len(priorities))])
    answer = 0
    maxN = max(priorities)
    while True:
        front = temp.popleft()
        if priorities[front] < maxN:
            temp.append(front)
        else:
            answer += 1
            priorities[front] = 0
            maxN = max(priorities)
            if front == location:
                return answer               

priorities = [2, 1, 3, 2]
#[1, 1, 9, 1, 1, 1]	
location = 2
#0

solution(priorities, location)