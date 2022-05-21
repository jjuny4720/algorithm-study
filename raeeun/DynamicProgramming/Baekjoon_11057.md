# 문제
---
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

<br>

# 입력
---
첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

<br>

# 출력
---
첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.

<br>

# 풀이 코드 (Java)
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P11057 {

    static int n;
    static int dp[][];

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        //dp[N][K] = N개 자리의 숫자 중 가장 맨뒤의 숫자가 K일때의 경우의 수
        dp = new int[n+1][10];

        for(int i = 0; i < 10; i++) {
            dp[1][i] = 1;
        }

        for(int i = 2; i <= n; i++) {
            for(int j = 0; j < 10; j++) {
                for(int k = 0; k <= j; k++) {
                    dp[i][j] += dp[i-1][k];
                    dp[i][j] %= 10007;
                }
            }
        }

        int res = 0;
        for(int i = 0; i < 10; i++) {
            res += dp[n][i];
        }
        System.out.println(res % 10007);

    }

}

```

<br>

# 코드 설명
---
+ dp[N][K] = N자릿수의 끝 숫자가 K인 경우의 오르막 수의 개수
+ 점화식 : dp[N][K] = Σ dp[N-1][M] (1 ≤ M ≤ K ≤ 9)

<br>

## 예제 1
>입력 : 1
출력 : 10

<br>

## 예제 2
>입력 : 2
출력 : 55

<br>

## 예제 3
>입력 : 3
출력 : 220