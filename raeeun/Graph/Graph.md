# 그래프 알고리즘이란?
---
+ 그래프 : 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조

||그래프|트리|
|---|---|---|
|방향성|방향 그래프 or 무방향 그래프|방향 그래프
|순환성|순환 및 비순환|비순환|
|루트 노드 존재 여부|루트 노드가 없음|루트 노드가 존재
|노드간 관계성|부모와 자식 관계 없음|부모와 자식 관계|
|모델의 종류|네트워크 모델|계층 모델|

<br>

# 구현 방법
---
**노드 개수 V, 간선 개수 E 일때**
<br>
+ 인접 행렬(Adjacency Matrix) : 2차원 배열을 사용하는 방식
```
O(V^2)만큼의 메모리 공간 필요
간선의 비용을 아는데 O(1)의 시간 소요
```

+ 인접 리스트(Adjacency List) : 리스트를 사용하는 방식
```
O(E)만큼의 메모리 공간 필요
간선의 비용을 아는데 O(V)만큼의 시간 소요
```

<br>

# 다양한 그래프 알고리즘
---
## 다익스트라 최단 경로 알고리즘
---
+ 인접 리스트(Adjacency List)를 이용하는 방식
+ 노드의 개수가 V개 일 때 V개의 리스트를 만들어 각 노드와 연결된 모든 간선에 대한 정보를 리스트에 저장
+ 최단 경로를 찾아야하는 문제에서, 노드와 간선의 개수가 많은 경우 우선순위 큐와 함께 사용

<br>

## 플로이드 와샬 알고리즘
---
+ 인접 행렬(Adjacency Matrix)을 이용하는 방식
+ 모든 노드에 대하여 다른 노드로 가는 최소 비용을 V^2 크기의 2차원 리스트에 저장한 뒤 해당 비용 갱신 -> 최단 거리 계산
+ 최단 경로를 찾아야하는 문제에서, 노드의 개수가 적은 경우 사용

<br>

## 서로소 집합 자료구조
----
+ 서로소 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
+ union(합집합), find(찾기) 두 가지 연산으로 조작 가능
-> union-find(합치기 찾기) 자료구조라고도 불림
+ 서로소 집합 계산 알고리즘
```
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
	1) A와 B의 루트 노드 A', B'를 각각 찾는다.
    2) A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다).
    
2. 모든 union(합집합) 연산을 처리할 때까지 1. 과정을 반복한다.
```

<br>

### 서로소 집합 자료구조 소스 코드
```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x) :
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x :
    	return find_parent(parent, parent[x])
    return x
    
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
	a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
    	parent[b] = a
    else :
    	parent[a] = b
        
# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1) :
	parent[i] = i
    
# union 연산을 각각 수행
for i in range(e) :
	a, b = map(int, input().split())
    union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1) :
	print(find_parent(parent, i), end=' ')
    
print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end='')
for i in range(1, v + 1) :
	print(parent[i], end=' ')
```

+ 경로 압축(Path Compression) 기법
	- 루트 노드만 저장, 직렬 탐색X, 바로 루트로 접근할 수 있게끔
    ```python
    def find_parent(parent, x) :
    	if parent[x] != x :
        	parent[x] = find_parent(parent, parent[x])
        return parent[x]
    ```
    
<br>

### 서로소 집합 알고리즘의 시간 복잡도
+ 경로 압축(Path Compression) 기법을 사용할 경우
	->O(M log N)
    
<br>

### 서로소 집합을 활용한 사이클 판별
+ 사이클 판별 알고리즘
```
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
	1) 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것이다.
    
2. 그래프에 포함되어 있는 모든 간선에 대하여 1. 과정을 반복한다.
```
<br>

### 서로소 집합을 활용한 사이클 판별 소스 코드
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x :
    	parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
	a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
    	parent[b] = a
    else :
    	parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1) :
	parent[i] = i
    
cycle = False # 사이클 발생 여부

for i in range(e) :
	a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b) :
    	cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else :
    	union_parent(parent, a, b)
        
if cycle :
	print("사이클이 발생했습니다.")
else :
	print("사이클이 발생하지 않았습니다.")
```

<br>

## 신장 트리 (Spanning Tree)
---
+ 신장 트리(Spanning Tree) : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

![](https://velog.velcdn.com/images/reyang/post/ef7a6844-c3b2-4d6f-86f3-e69c66b61ab6/image.png)

<br>

### 크루스칼 알고리즘 (Kruskal Algorithm)
+ 최소 신장 트리 알고리즘 : 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘 
+ 가장 적은 비용으로 모든 노드를 연결할 수 있음
+ 최소 신장 트리 알고리즘
```
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.

2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인한다.
	1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    
3. 모든 간선에 대하여 2.번의 과정을 반복한다.
```
+ 최소 신장 트리는 일종의 트리 자료구조
	-> E = V - 1
    
<br>

### 크루스칼 알고리즘 소스코드
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x :
    	parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
	a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
    	parent[b] = a
    else :
    	parent[a] = b
        
# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)	# 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1) :
	parent[i] = i
    
# 모든 간선에 대한 정보 입력받기
for _ in range(e) :
	a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges :
	cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b) :
    	union_parent(parent, a, b)
    	result += cost
        
print(result)
```
<br>

### 크루스칼 알고리즘의 시간 복잡도
+ 간선의 개수 E일 경우, O(E log E)
+ 크루스칼 알고리즘을 적용하기 위한 간선 정렬 작업의 시간 복잡도가 O(E log E)임
+ (크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도 < 정렬 알고리즘의 시간 복잡도) 이므로 무시

<br>

## 위상 정렬
---
+ 위상 정렬 : 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
+ 진입차수(indegree) : 특정 노드로 '들어오는' 간선의 개수

<br>

### 위상 정렬 알고리즘
```
1. 진입차수가 0인 노드를 큐에 넣는다.

2. 큐가 빌 때까지 다음의 과정을 반복한다.
	1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    2) 새롭게 진입차수가 0이 된 노드를 큐에 넣음
```
+ 위상 정렬의 결과 : 큐에서 꺼낸 원소의 순서

<br>

### 위상 정렬 소스코드
```python
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e) :
	a, b = map(int, input().split())
    graph[a].append(b)	# 정점 A에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1
    
# 위상 정렬 함수
def topology_sort() : 
	result = []	# 알고리즘 수행 결과를 담을 리스트
    q = deque()	# 큐 기능을 위한 deque 라이브러리 사용
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1) :
    	if indegree[i] == 0 :
        	q.append(i)
            
    # 큐가 빌 때까지 반복
    while q :
    	# 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now] :
        	indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] = 0 :
            	q.append(i)
                
# 위상 정렬을 수행한 결과 출력
for i in result:
	print(i, end=' ')
    
topology_sort()
```

<br>

### 위상 정렬의 시간 복잡도
+ O(V + E)
+ 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거해야 함