n = int(input())

dp = [1] * 10

for _ in range(n-1):
    for i in range(1,10):
        dp[i] = (dp[i] + dp[i-1]) % 10007
print(sum(dp) % 10007)