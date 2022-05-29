# 문제
---
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

<br>

# 입력
---
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

<br>

# 출력
---
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

<br>

# 요약
> 입력 : V(정점의 개수) E(간선의 개수)
K(시작 정점 번호)
u v w (u->v인 가중치 w인 간선)
.
.
출력 : i번째 줄에 i번 정점으로의 최단 경로의 경로값 출력
(자기 자신은 0, 경로가 없다면 INF 출력)

<br>

# 문제 풀이 (Java)
---
```java
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1753 {

    static class Edge implements Comparable<Edge> {
        //id : 정점 번호, cost : 정점간의 거리
        int id, cost;

        public Edge(int id, int cost){
            this.id = id;
            this.cost = cost;
        }

        //우선순위 큐의 정렬 기준 정의
        @Override
        public int compareTo(Edge o){
            //오름차순으로 정렬 (최단거리가 가장 앞으로 가도록)
            return this.cost - o.cost;
        }

    }
    static int V, E, K;
    static int u, v, w;
    static int [] dist;
    static ArrayList[] adjList;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //정점 개수 V, 간선 개수 E, 시작 노드 번호 K
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        //최단거리 테이블 초기화
        dist = new int[V+1];
        for(int i = 0; i < dist.length; i++) {
            dist[i] = Integer.MAX_VALUE;
        }

        //인접 정점 리스트 초기화
        adjList = new ArrayList[V+1];
        for(int i = 0; i < adjList.length; i++) {
            adjList[i] = new ArrayList<Edge>();
        }

        //인접 정점 리스트 입력
        for(int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            adjList[u].add(new Edge(v, w));
        }

        //다익스트라 알고리즘 수행
        dijkstra(K);

        //출력
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i <= V; i++) {
            if(dist[i] == Integer.MAX_VALUE) {
                sb.append("INF\n");
            }
            else {
                sb.append(dist[i]+"\n");
            }
        }

        System.out.println(sb.toString().trim());

    }

    static void dijkstra(int start) {

        PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
        //자기 자신과의 거리는 0
        dist[start] = 0;
        //우선순위 큐에 먼저, 자신과의 거리를 넣음
        pq.add(new Edge(start, 0));

        while(!pq.isEmpty()) {
            Edge cur = pq.poll();

            //dist에 저장되어 있는게 최단 경로가 맞으면 continue
            if(cur.cost > dist[cur.id]) {
               continue;
            }
            
            //아니라면 cur에 연결되어 있는 모든 정점들 사이에서의 최단 경로를 갱신함
            for(int i = 0; i < adjList[cur.id].size(); i++) {
                Edge next = (Edge)adjList[cur.id].get(i);
                //더욱 최단 경로인 것으로 갱신하고 pq에 넣기
                if(dist[next.id] > cur.cost + next.cost) {
                    dist[next.id] = cur.cost + next.cost;
                    pq.add(new Edge(next.id, dist[next.id]));
                }
            }
        }

    }

}
```

<br>

## 예제 1
> 입력 :
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
출력 :
0
2
3
7
INF