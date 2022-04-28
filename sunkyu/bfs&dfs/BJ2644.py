# 백준 2644 촌수계산 (실버 2)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

matrix = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
  x, y = map(int, input().split())
  matrix[x].append(y)
  matrix[y].append(x)

def bfs(node):
  queue = deque()
  queue.append(node)
  visited = [0 for _ in range(n+1)]
  visited[node] = 1
  while queue:
    d = queue.popleft()
    for i in matrix[d]:
      if visited[i] == 0:
        visited[i] = 1
        result[i] = result[d] + 1
        queue.append(i)

bfs(a)
print(result[b] if result[b] != 0 else -1) 