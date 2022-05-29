# 최단 경로

> 특정 지점까지 가장 빠르게 도달하는 알고리즘

## 가장 빠른 길 찾기

### 가장 빠르게 도달하는 방법

**최단 경로** 알고리즘은 말 그대로 가장 짧은 경로를 찾는 알고리즘이다. 길 찾기 문제라고도 불린다.  

- 한 지점애서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우   

이러한 사례에 맞는 알고리즘을 알고 있다면 문제를 좀 더 쉽게 풀 수 있다.  

### 다익스트라 최단 경로 알고리즘

> 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘

- 음의 간선이 없을 때 정상적으로 작동한다.
- 음의 간선이란 0보다 작은 값을 가지는 간선을 의미함
- 그리디 알고리즘
- 매번 '가장 비용이 적은 노드'를 선택해서 임의의 과정을 반복하기 때문

**알고리즘의 원리**

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3과 4번을 반복한다.

- 다익스트라 알고리즘은 최단 경로를 구하는 과정에서 '각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다는 특징이 있다.
- 구현하기 쉽자민 느리게 동작하는 코드
- 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드
- 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

**방법 1. 간단한 다익스트라 알고리즘**

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index =  0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j
            # 현재 노드를 거챠서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

**방법 2. 개선된 다익스트라 알고리즘**

```python
# 9-2.py 개선된 다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 개수를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한을 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 었는 경우 거리를 출력
    else:
        print(distance[i])
```

### 플로이드 워셜 알고리즘

> 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용

- 알고리즘 단계마다 거쳐가는 노드를 기준으로 알고리즘을 수행
- 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다는 점이 다르다.
- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍
- 점화식에 맞게 2차원 리스트를 갱신한다.

```python
# 9-3.py 플로이드 워셜 알고리즘 소스코드
import sys
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())
# 2차원 리스트 만들기
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C 라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
print()
```

### 연습문제 풀이 (프로그래머스 - 배달)

**문제설명**

N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다.  
각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다.  
도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.  
각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.  
다음은 N = 5, K = 3인 경우의 예시입니다.

**제한사항**

- 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
- road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
- road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
- road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
- a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
- 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
- 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
- K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
- 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
- 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.

**접근방식**

- 한 지점에서 다른 모든 지점까지의 최단 경로를 구해 k이하인 것의 개수를 구한다.

**코드**

```python
import heapq

def dks(v, graph, dp):
    q = []
    # 현재 가장 가까운 노드를 저장하기 위한 목적으로 우선순위 큐 사용
    heapq.heappush(q, (0, 1)) #cost, start
    dp[1] = 0
    
    while q:
        # 현재 정점까지의 비용 : cost 
        w, n = heapq.heappop(q)
        
        # 현재 정점까지의 비용 + 현재 정점에서 다음 정점까지의 비용 c = 다음 노드 까지의 비용
        for ad_n, ad_w in graph[n]:
            ww = w + ad_w
            # 다음 노드까지의 비용이 기록된 값보다 작으면 조건 성립
            if ww < dp[ad_n]:
                dp[ad_n] = ww#업데이트
                heapq.heappush(q, (ww, ad_n))
    return dp
    
    
def solution(N, roads, K):
    ans = 0
    graph = [[] for _ in range(N+1)]
    
    # 양방향
    for start, end, time in roads:
        graph[start].append((end, time))
        graph[end].append((start, time))
    
    # N번 노드까지 오는 비용
    dp = [1e9]*(N+1)
    
    result = dks(1, graph, dp)
    for re in result:
        if re <= K:
            ans += 1
            
    return ans
```

- graph : 연결 관계를 저장할 2차원 리스트인 graph에 노드와 걸리는 시간 순으로 저장한다.  
  - 양방향 관계로 저장
- dp : 최단 거리를 저장할 dp 테이블을 만들고 무한대인 1e9로 초기화
- 다익스트라 사용 : 교재 참고함
  - 우선순위 큐 사용 (heapq 모듈 사용)