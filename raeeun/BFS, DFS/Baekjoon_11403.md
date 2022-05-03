# 문제
---
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
<br>

# 입력
---
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.
<br>

# 출력
---
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
<br>

# 문제 요약
>정점의 개수 N  (1 ≤ N ≤ 100)
<br>
입력 : N
(N줄에 걸친 인접행렬)
출력 : 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력

<br>

# 풀이 코드 (Java)
---
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class q11403 { //플로이드 와샬 알고리즘 
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] check = new int[n][n];
		
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				check[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
        //플로이드 와샬 알고리즘 
		//거쳐가는 노드 k
		for(int k = 0; k < n; k++) {
			//출발 노드 i
			for(int i = 0; i < n; i++) {
				//도착 노드 j
				for(int j = 0; j < n; j++) {
					if(check[i][k] == 1 && check[k][j] == 1) {
						check[i][j] = 1;
					}
				}
			}
		}
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.printf("%d ", check[i][j]);
			}
			System.out.println();
		}

	}

}
```
<br>

# 코드 설명
---
+ 플로이드 와샬 알고리즘 사용
+ 다익스트라 알고리즘 : 하나의 정점에서 출발했을 때, 다른 모든 정점으로의 최단 경로를 구하는 경우
+ 플로이드 와샬 알고리즘 : 거쳐가는 정점을 기준으로 모든 정점에서 모든 정점으로의 최단 경로를 구하는 경우
+ i부터 j까지의 최단 경로 VS i부터 k까지의 최단 경로 + k부터 j까지의 최단 경로

<br>

## 예제 1
---
>입력 :
3
0 1 0
0 0 1
1 0 0
출력 :
1 1 1
1 1 1
1 1 1

## 예제 2
---
>입력 :
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
출력 : 
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0