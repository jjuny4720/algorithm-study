# 정렬

## 기준에 따라 데이터를 정렬

### 정렬 알고리즘 개요

**정렬**이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것  
프로그램을 작성할 때 가장 많이 사용되는 알고리즘 중 하나이다.

많이 사용하는 정렬 알고리즘

- 선택 정렬
- 삽입 정렬
- 퀵 정렬
- 계수 정렬

파이썬에서 제공하는 기본 정렬 라이브러리까지  
면접 단골 질문이기도 하다

### 선택 정렬

**가장 작은 데이터를 *선택*한다**

> 데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다.

```python
# 6-1.py 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i+1, len(array)):
    if array[min_index]>array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스왑

print(array)
```

**선택 정렬의 시간 복잡도는 O(N^2)**

### 삽입 정렬

알고리즘 문제 풀이에 사용하기네는 느린 편

> 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?

삽입 정렬은 동작 원리를 직관적으로 이해하기 쉬운 알고리즘이다.
하지만 구현 난이도는 어려움

- 삽입 정렬은 필요할 때만 위치를 바꾸므로 데이터가 거의 정렬되어 있을 때 효율적
- 특정한 데이터를 적절한 위치에 삽입한다.
- 데이터가 적절한 위치에 들어가기 이전에, 그 앞의 데이터는 모두 정렬되어 있다고 가정한다.

```python
# 6-3.py 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  # 인덱스 i부터 1까지 감소하며 반복되는 작업
  for j in range(i, 0, -1):
    # 한 칸씩 왼쪽으로 이동
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
    else:
      break

print(array)
```

**삽입 정렬의 시간 복잡도는 O(N^2)**

### 퀵 정렬

가장 많이 사용되는 알고리즘 (빠른 편)
비슷하게 빠른 알고리즘은 병합정렬

> 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.

퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.

- 퀵 정렬에서는 피벗이 사용됨
- 큰 숫자와 작은 숫자를 교환하기 위한 기준이 피벗
- 리스트에서 첫 번째 데이터를 피벗으로 정함
- 왼쪽에서부터 5보다 큰 수를 찾고
- 오른쪽에서부터 5보다 작은 수를 찾는다.
- 찾았으면 두 위치를 변경
- 반복하다가 엇갈리면 작은 수와 피벗을 변경
- 피벗을 기준으로 개별 파티션을 퀵 정렬
- 현재 리스트의 개수가 1개이면 정렬완료라고 판단

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  # 원소가 1개인 경우 종료
  if start>=end:
    return
  # pivot은 첫번째 원소
  pivot = start
  left = start + 1
  right = end
  while left<=right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left<=end and array[left]<=array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right>start and array[left] >= array[pivot]:
      right -= 1
    #엇갈렸다면 작은 데이터와 피벗을 교체
    if left>right:
      array[right], array[pivot] = array[pivot], array[right]
    #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    else:
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quic_sort(array, start, right-1)
  quic_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```

```python
# 6-5.py 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  #리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if ]
```
