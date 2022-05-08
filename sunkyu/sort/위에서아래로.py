import sys

input = sys.stdin

n = int(input())
array = []

for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for obj in array:
  print(obj, end=' ')