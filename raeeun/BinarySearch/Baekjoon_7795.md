# 문제
---
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.

![](https://velog.velcdn.com/images/reyang/post/029dca39-e3b9-4b10-9504-305e7b24e19a/image.png)

두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

<br>

# 입력
---
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 

<br>

# 출력
---
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.

<br>

# 문제 요약
>입력 : t (테스트 케이스)<br>n (A의 원소 개수), m (B의 원소 개수)
(n개의 줄에 A의 원소들)
(m개의 줄에 B의 원소들)
.
.
출력 : 각 테스트 케이스에 대한 A의 원소 > B의 원소일 경우의 순서쌍 개수

<br>

# 문제 풀이 (Java)
---

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class P7795 {

    //A의 원소 > B의 원소인 경우 리턴
    static int BinarySearch(int target, int[] arr){

        int count = 0;
        int start = 0;
        int end = arr.length-1;

        while(start <= end) {

            int mid = (start + end)/2;

            if(arr[mid] < target) {
                count = mid + 1;
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }

        }
        
        return count;
        
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {

            int count = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[] A = new int[n];
            int[] B = new int[m];
            
			//배열 A에 A의 원소들 할당
            st = new StringTokenizer(br.readLine());
            for(int i=0; i<n; i++) {
                A[i] = Integer.parseInt(st.nextToken());
            }

			//배열 B에 B의 원소들 할당 
            st = new StringTokenizer(br.readLine());
            for(int i=0; i<m; i++) {
                B[i] = Integer.parseInt(st.nextToken());
            }

			//B를 정렬
            Arrays.sort(B);

			//각 테스트 케이스마다 정답 append
            int result = 0;
            for(int i=0; i<A.length; i++){
                result += BinarySearch(A[i], B);
            }
            sb.append(result+"\n");

        }

        System.out.println(sb.toString().trim());

    }

}
```
<br>

# 코드 설명
---
+ 이진 탐색 알고리즘 사용
+ A와 B를 받고 B를 정렬시킨 후, A의 원소들을 하나씩 돌아가면서 B에 대한 이진 탐색을 시작
+ 각 테스트 케이스마다 이진 탐색을 하면서 A의 원소 > B의 원소인 경우의 순서쌍의 개수를 append한 후 출력

<br>

## 예제 1
---
>입력 :
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215<br>
출력 :
7
1