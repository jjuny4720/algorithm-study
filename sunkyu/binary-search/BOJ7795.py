import sys
import bisect

input = sys.stdin.readline
t = int(input())
for _ in range(t):
  count = 0
  n, m = input().split()
  a = sorted(list(map(int, input().split())))
  b = sorted(list(map(int, input().split())))
  for item in a:
    count += bisect.bisect_left(b, item)
  print(count)
  