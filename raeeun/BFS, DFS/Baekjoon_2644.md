# 문제
---
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
<br>

# 입력
---
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.
<br>

# 출력
---
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.
<br>

# 문제 요약
>
입력 : 전체 사람의 수 n
촌수 계산할 사람 두 명
부모 자식 관계 수 m
m개의 줄에 부모 자식 관계가 주어짐
<br>
출력 : 촌수 계산 결과

<br>

# 문제 풀이 (Java)
---
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class q2644 {

	static int n, a, b, m;
	static ArrayList<Integer>[] matrix;
	static boolean[] visited;
	static int result = -1;
	
	static void dfs(int node, int cnt) {
		
		visited[node] = true;
		for(int i = 0; i < matrix[node].size(); i++) {
			int next = matrix[node].get(i);
			
			if(next == b) {
				result = cnt;
				return;
			}
			if(!visited[next]) {
				dfs(next, cnt+1);
			}
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		visited = new boolean[n+1];
		matrix = new ArrayList[n+1];
		for(int i = 0; i <= n; i++) {
			matrix[i] = new ArrayList<Integer>();
		}
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			matrix[x].add(y);
			matrix[y].add(x);
		}
		
		dfs(a, 0);
		
		System.out.println(result==-1?-1:result+1);
		
	}

}
```
<br>

# 코드 설명
---
+ 재귀로 구현한 DFS 사용
+ 행렬로 구현 X 
+ 일차원 배열에 ArrayList 넣음 -> 촌수로 이어진 노드들 저장
+ DFS 함수 :
현재 노드 cur, 끝 노드 end
기본 단계 : 현재 탐색한 노드가 end라면 현재 count 리턴
재귀 단계 : 현재 탐색한 노드가 end가 아니라면
count+1을 한 뒤, cur에 연결되어 있는 노드 탐색

<br>

## 예제 1
---
>입력 :
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
출력 : 3

<br>

## 예제 2
---
>입력 :
9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
출력 : -1