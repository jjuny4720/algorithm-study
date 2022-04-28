# 백준 11403번 경로 찾기 (실버 1)

import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
  for j in range(n):
    for k in range(n):
      if matrix[j][i] and matrix[i][k]:
        matrix[j][k] = 1

for i in range(n):
  print(*matrix[i])
