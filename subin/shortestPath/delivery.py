import heapq as hq
def solution(N, road, K):
    answer = 0
    start = 1
    INF = int(1e9)
    graph = [[] for i in range(N+1)]
    distance = [INF] * (N+1)
    
    for r in road:
        a,b,c = r
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distance[start] = 0
    q = []
    hq.heappush(q,(0,start))
    
    #다익스트라 알고리즘
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        for g in graph[now]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                hq.heappush(q,(cost,g[0]))

    for i in range(1,N+1):
        if distance[i] <=K:
            answer +=1
            
    return answer