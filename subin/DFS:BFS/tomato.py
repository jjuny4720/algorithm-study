from collections import deque

queue = deque()

m, n = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
    # for j in range(m):
    #         if matrix[i][j] == 1:
    #             queue.append([i, j])
    
for i in range(n):
    for j in range(m):
            if matrix[i][j] == 1:
                queue.append([i, j])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))
         
bfs()

max = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(-1)
            exit()
        if matrix[i][j] > max:
            max = matrix[i][j]
print(max - 1)
