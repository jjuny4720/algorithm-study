import heapq as hq

def solution(n, edge):
    graph = [[] for i in range(n+1)]
    for a, b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
        
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[1] = 0
    q = []
    hq.heappush(q,(0,1))
    
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q,(cost,i[0]))
                
    far = max(distance[1:])
    return distance.count(far)