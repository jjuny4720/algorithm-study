# 가장 먼 노드
"""
- n개의 노드가 있는 그래프가 있다.
- 각 노드는 1부터 n까지 번호가 적혀있다.
- 1번노드에서 가장 멀리 떨어진 노드의 개수를 구하려고 한다.
- 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.
---
- 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때
- 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return
"""

from collections import deque


def solution(n, edge):
    # 변수 초기화
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    queue = deque([(1, 0)])

    # 그래프 입력
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    # 큐를 도는 동안
    while queue:
        # 맨 앞 빼옴
        vertex, dist = queue.popleft()
        # 방문여부가 false 라면
        if visited[vertex] == -1:
            # 거리 삽입
            visited[vertex] = dist
            # 각 정점을 돌면서
            for obj in graph[vertex]:
                # 큐에 추가
                queue.append((obj, dist + 1))

    # visited를 돌면서
    for i in range(len(visited)):
        # 거리가 최댓값이라면
        if visited[i] == max(visited):
            # 답임
            answer += 1

    return answer