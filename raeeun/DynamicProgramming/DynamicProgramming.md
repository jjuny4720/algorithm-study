# 다이나믹 프로그래밍이란?
---
+ 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘
+ 동적 계획법이라고도 표현
+ 2가지 방식 (탑 다운, 바텀 업)

<br>

# 다이나믹 프로그래밍
---
+ 밑으로는 다이나믹 프로그래밍으로 해결할 수 있는 문제들

<br>

## 피보나치 수열
---
+ 이전 두 항의 합을 현재 항으로 설정하는 특징
+ f (x) + f (x + 1) = f (x + 2)

![](https://velog.velcdn.com/images/reyang/post/5a599b12-59b7-461e-a209-5ec9fc6b76f8/image.png)

프로그래밍에서는 이러한 수열을 **배열** 또는 **리스트**로 표현할 수 있다.
C/C++, Java -> 배열으로 구현
Python -> 리스트로 구현

<br>

### 피보나치 함수 코드 (Java)
---
```java
public int Fibo(int x) {

	if(x == 1 || x == 2) {
    	return 1;
    }
    
    return Fibo(x - 1) + Fibo(x - 2);

}
```

해당 소스코드는 f(n)함수의 n이 커질수록 수행 시간이 급격하게 늘어난다는 단점이 있다.
시간 복잡도 : O(2^N)
예를 들어 N=30일때, 약 10억 가량의 연산을 수행해야 한다.

+ f(6)일 때의 피보나치 함수 호출 과정
![](https://velog.velcdn.com/images/reyang/post/ca8b8acb-578a-4ea6-ad18-19a0e2c80c13/image.png)
f(6)을 구하는 과정에서 f(3)이 3번, f(2)가 5번 호출됨
따라서, 다이나믹 프로그래밍은 f(3)이나 f(2)같은 값들을 중복 탐색할 필요 없이 미리 저장해두고 사용함

<br>

### DP 피보나치 함수 코드 (Java)
---
```java
static int n;
static int dp[];

static int Fibo(int x) {

    if(x == 1 || x == 2) {
        return 1;
    }

    if(dp[x] == 0) {
        dp[x] = Fibo(x - 1) + Fibo(x - 2);
    }

    return dp[x];

}

public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    dp = new int[n + 1];

    System.out.println(Fibo(n));

}
```
+ dp라는 배열 dp[n] 공간에 f(n)값을 할당
+ 재귀 함수를 호출하기 전에 dp에 찾으려는 값이 있는지 확인한 후 있으면 dp를 리턴, 없다면 재귀 함수 호출
	-> 중복되는 탐색 작업이 필요 없음

<br>

# 재귀와 반복문
---
+ 탑다운(Top down) : 재귀를 사용하여 큰 문제를 작은 문제로 나누어 풀어가는 방식
+ 바텀업(Bottom up) : 반복문을 사용하여 작은 문제들로 큰 문제를 풀어가는 방식

<br>

# 다이나믹 프로그래밍 풀이 단계
---
1. 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하기
	+ 완전 탐색 알고리즘으로 접근했을 때 시간이 매우 오래 걸리면 다이나믹 프로그래밍으로 적용 가능한지 파악하기
    + 해결하고자 하는 부분 문제들의 중복 여부 확인하기
    

2. 단순한 재귀 함수로 비효율적인 코드를 작성한 뒤, 작은 문제에서 구한 답이 큰 문제에서 활용할 수 있다면 (메모리제이션이 적용 가능하다면) 코드를 개선하는 방법도 있음

<br>

! 가능하다면 탑다운 방식보다는 바텀업 방식을 권유
- 시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있음