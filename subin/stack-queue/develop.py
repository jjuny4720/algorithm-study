def solution(progresses, speeds):
    answer = []
    stack = []
    day = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            day = (100 - progresses[i]) // speeds[i]
        else:
            day = int((100 - progresses[i]) / speeds[i] + 1)
        
        if i == 0:
            stack.append(day)
        else:
            if stack[0] >= day:
                stack.append(day)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(day)

    answer.append(len(stack))
        
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)