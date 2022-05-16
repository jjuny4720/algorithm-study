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