# 이진 탐색

> 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘

## 범위를 반씩 좁혀가는 탐색

### 순차 탐색

> 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 데이터를 찾을 수 있다.

```python
# 7-1.py 순차 탐색 소스코드
def sequential_search(n, target, array):
  # 각 원소를 하나씩 확인하여
  for i in range(n):
    # 현재의 원소가 찾고자 하는 원소와 동일한 경우
    if array[i] == target:
      return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띅 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

**시간복잡도 O(N)**

### 이진 탐색 : 반으로 쪼개면서 탐색하기

> 이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점이다.  
> 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이 이진 탐색 과정이다.

**한 번 확인할 때마다 원소의 개수가 반으로 줄어 시간 복잡도는 O(logN)**

```python
# 7-2.py 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(arrray, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 찾은 경우 인덱스 번환
  if array[mid] == target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)
```

```python
# 7-3.py 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)
```

### 코딩 테스트에서의 이진 탐색

- 바로 이진탐색의 소스코드를 구현하는 것은 어렵다.
- 코드 작성이 단골로 나와서 가급적 외워야 함

### 트리 자료구조

- 트리는 부모 노드와 자식 노드의 관계를 표현된다.
- 트리의 최상단 노드를 루트 노드라고 한다.
- 트리의 최하단 노드를 리프 노드라고 한다.
- 트리에서 일부를 떼어내도 트리 구조이면 이를 서브 트리라고 한다.
- 트리는 파일 시스템과 같이 계층적이도 정렬된 데이터를 다루기에 적합하다.

> 큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진 탐색과 같은 탐색 기법을 이용해 빠르게 탐색이 가능하다.

### 이진 탐색 트리

이진 탐색 트리의 특징

- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다.

### 빠르게 입력받기

- input() 함수는 느림
- sys 라이브러리의 readline() 함수를 이용
- readline() 함수를 사용하면 rstrip() 함수 호출

```python
# 7-4.py 한 줄 입력받아 출력하는 소스코드
import sys

input_data = sys.readline().rstrip()
print(input_data)
```
