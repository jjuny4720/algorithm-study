# 이진탐색 알고리즘이란?
---
+ 범위를 반씩 좁혀가는 탐색
<br>

## 순차 탐색
---
+ 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 **차례대로** 확인하는 방법

![](https://velog.velcdn.com/images/reyang/post/d8f8ad95-c923-4997-ae7e-3ecb26a2baea/image.png)

+  코드 (Java)

```java
static int LinearSearch( int target, int[] arr ) {

	for( int i = 0; i < arr.length; i++ ){
    
    	if( target == arr[i] ){
        	return i;
        }
        
    }

}
```
+ 시간복잡도 : O(N)

<br>

## 이진 탐색
---
+ 위치를 나타내는 변수 3개를 사용 (시작점, 끝점, 중간점)

![](https://velog.velcdn.com/images/reyang/post/ecc7a7a7-f957-494c-93a2-8332f8357337/image.png)

+ 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정

+ 코드 (Java)
```java
static int BinarySearch ( int target, int[] arr ) {

	int start = 0;
    int end = 0;
    
    while ( start <= end ) {
    	
        int mid = ( start + end ) / 2;
        
        if ( arr[mid] < target ) {
        	end = mid - 1;
        }
        else {
        	start = mid + 1;
        }
    
    }
    
    return mid;

}
```
+ 시간복잡도 : O(log N)

<br>

# 코딩 테스트에서의 이진 탐색
---
+ 높은 난이도의 문제는 이진 탐색 알고리즘이 다른 탐색 알고리즘과 같이  사용되기도 함
+ 탐색 범위가 2000만을 넘어가는 경우, 이진 탐색으로 접근하기
+ 이진 탐색 코드 암기 권유

<br>

# 이진 탐색 트리
---
+ 효율적인 탐색이 가능한 자료구조

![](https://velog.velcdn.com/images/reyang/post/694456f4-6b64-425a-a1cd-92137902599d/image.png)
+ 부모 노드보다 왼쪽 자식 노드가 작다.
+ 부모 노드보다 오른쪽 자식 노드가 크다.
+ 즉, **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드**
