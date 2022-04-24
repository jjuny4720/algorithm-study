def solution(numbers, target):
    answer = 0

    def dfs(i, sum):
        if i == len(numbers):
            if sum == target:
                nonlocal answer
                answer += 1
        else:
            dfs(i+1, sum + numbers[i])
            dfs(i+1, sum - numbers[i])

    dfs(0, 0)

    return answer