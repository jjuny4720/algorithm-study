def solution(numbers, target):
    answer = 0
    def dfs(sum, level):
        nonlocal answer

        if level == len(numbers):
            if sum == target:
                answer += 1
            return

        signed = [-sum, sum]

        if level == 1:
            for i in range(2):
                dfs(signed[i]+numbers[level], level+1)
                dfs(signed[i]-numbers[level], level+1)
        else:
            dfs(sum+numbers[level], level+1)
            dfs(sum-numbers[level], level+1)
    dfs(numbers[0], 1)

    return answer