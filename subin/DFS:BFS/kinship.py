n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(n):
    for i in graph[n]:
        if(visited[i] == 0):
            visited[i] = visited[n]+1
            dfs(i)

dfs(a);

print(visited[b] if visited[b] > 0 else -1)