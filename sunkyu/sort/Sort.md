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

  # 피벗은 첫 번째 원소
  pivot = array[0]
  # 피벗을 제외한 리스트
  tail = array[1:]

  # 분할된 왼쪽 부분
  left_side = [x for x in tail if x <= pivot]
  # 분할된 오른쪽 부분
  right_side = [x for x in tail if x > pivot]

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각깍 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

**퀵 정렬의 시간 복잡도는 O(NlogN)**

### 계수 정렬

> 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘

- 일반적으로 뵬도의 리스트를 선언하고
- 그 안에 정렬에 대한 정보를 담는다는 특징이 있다.
- 계수 정렬은 데이터의 크기가 제한되어 있을 떄에 한해서 데이터의 개수가 매우 많더라도 빠르게 동작

```python
# 6-6.py 계수 정렬 소스코드
# 모든 원소의 값이 -보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  # 각 데이터에 해당하는 인덱스의 값 증가
  count[array[i]] += 1

for i in range(len(count)):
  # 리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
    print(i, end=' ')
```

**계수 정렬의 시간 복잡도는 O(N+K)**

### 파이썬의 정렬 라이브러리

```python
# 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
# 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 O(NlogN)을 보장한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
```

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)
```

- 또한 sorted()나 sort()를 이용할 때에는 key 매개면수를 입력으로 받을 수 있다.
- key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다.
- 예를 들어 리스트의 데이터가 튜플로 구성되어 있을 때, 각 데이터의 두 번째 원소를 기준으로 설정하는 경우
- 다음 형태의 소스코드를 작성할 수 있다. 혹은 람다 함수를 사용 가능

```python
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

result = sorted(array, ket=setting)
print(result)
```

> 코딩 테스트에서 정렬 알고리즘이 사용되는 경우
>
> 1. 정렬 라이브러리로 풀 수 있는 문제  
>    단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
> 2. 정렬 알고리즘의 원리에 대해서 물어보는 문제  
>    선택정렬, 삽입정렬, 퀵정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
> 3. 더 빠른 정렬이 필요한 문제  
>    퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.

```python
# 위에서 아래로
import sys

input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for obj in array:
  print(obj, end=' ')
```

```python
# 성적이 낮은 순서로 학생 출력하기
import sys

input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1]))

array = sorted(array, key=lambda x: x[1])

for obj in array:
  print(obj[0], end=' ')
```

```python
# 두 배열의 원소 교체
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
```

## 연습문제 풀이

### 가장 큰 수

**문제 설명**

> 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요
>
> 예를 들어, 주어진 정숙가 [6, 10, 2]라면 [6102, 6120, 1062, 1026, 2610, 2106]을 만들 수 있고, 이중 가장 큰 수는 6210입니다.
>
> 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

**제한 사항**

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

**문제 해결을 위한 아이디어**

- 정렬을 하면 좋은데 무턱대고 하자니 두자리 이상의 숫자들이 걸린다.
- numbers의 원소는 1,000 이하이기 때문에 10으로 나누어 자리수를 판별해야 한다.
- 1의자리, 10의자리, 100의자리, 1000의자리로 각각 배열을 만들어 첫 번째 수가 제일 큰 것을 맨 앞으로 pop한다.
- 이를 반복한다.

```python
def solution(numbers):
    numbers.sort()
    max = 0
    answer = ''
    for i in range(len(numbers)):
        for number in numbers:
            if len(str(number)) == 1:
                if max<number:
                  max = number
            elif len(str(number)) == 2:
                if max<(number//10):
                  max = number
                elif max == (number//10):
                  if number%10 > max:
                    max = number
            elif len(str(number)) == 3:
                if max<(number//100):
                  max = number
                elif max == (number//100):
                  if number%100 > max:
                    max = number
            else:
                if max<(number//1000):
                  max = number
                elif max == (number//1000):
                  if number%1000 > max:
                    max = number
        numbers.remove(max)
        answer += str(max)
        max = 0
    return answer
```

- 시간 초과가 발생한 코드
- O(N^2)의 시간복잡도는 조금 아닌 것 같아서 다시 작성했다.
- 새로 문제가 되었던 부분은 3 30을 비교하는 부분
- 싹 지우고 다시 작성했다
- 나머지를 구하는 방식으로 3과 30 301 등을 비교하는 건 아닌 것 같았다.

```python
def solution(numbers):
  answer = ''
  numbers_list = [str(number) for number in numbers]
  numbers_list.sort(key=lambda number:number*3, reverse=True)
  answer = str(int(''.join(numbers_list)))
  return answer
```

- 통과한 풀이
- 3과 30, 301 등을 나머지로 비교하는 방식이 잘못된 것 같아서 다른 방식을 생각했다.
- 리스트를 문자열로 변환해 준 뒤에 같은 수를 3번 반복해주는 방식으로 정렬했다.
