# 백준 11057 오르막 수
import sys

input = sys.stdin.readline

n = int(input())

# 표를 그려서 규칙을 찾는다
d = [[0] * 10 for _ in range(1001)]
for i in range(10):
    d[0][i] = 1

for i in range(1, n+1):
    d[i][0] = 1
    for j in range(1, 10):
        d[i][j] = d[i - 1][j] + d[i][j - 1]

print((sum(d[n-1])) % 10007)