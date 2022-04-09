# 그리디 알고리즘

그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미

프로그래머스 체육복 

[코딩테스트 연습 - 체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)

첫번째 시도

```python
def solution(n, lost, reserve):
    answer = 0
    
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    for j in reserve:
        if j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
            
    answer = n - len(lost)
    
    return answer
```

테스트 케이스 두 개를 통과하고 제출 후 채점해 보았더니 테스트 케이스 20개 중 3개 정도 실패하였다.

문제의 조건을 살펴보면, 

`여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.`

라는 조건이 있어 lost와 reserve의 중복을 삭제한다.

체육복을 빌려줄 수 있는 학생을 기준으로 앞 학생이 체육복이 없다면, 체육복을 앞 학생에게 빌려주고, 뒤 학생이 체육복이 없다면 뒤 학생에게 빌려준다.

#### 원인 파악 1)

n = 5

lost = [2,4]

reserve = [3,1]

result = 5

이 테스트 케이스를 사용해 실행해 보았더니 result 값이 4를 return 하고 있었다.

reserve가 오름차순 정렬 되어 있길 가정해서 문제를 풀었기 때문에 이런 상황이 발생한 것 같다. 

#### 원인 파악 2) 

여유분을 가지고 있는 학생은 다른 친구를 챙기기 전에 우선 자기부터 입어야 한다 !

재시도 

```python
def solution(n, lost, reserve):

    reserve.sort()
    
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    for j in reserve:
        if j in lost:
            lost.remove(j)
        elif j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
            
    answer = n - len(lost)
    
    return answer
```

얻은 교훈 : 조건을 잘 생각하자! 충분한 테스트 케이스가 중요하다.

### 다른 풀이

[[Python] 프로그래머스 - 체육복](https://rain-bow.tistory.com/30)

set을 이용해 풀수도 있다. 

set : 중복을 허용하지 않는 집합 자료형
