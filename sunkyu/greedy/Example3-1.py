# 예제 3-1 거스름돈

import sys

n = int(sys.stdin.readline())
coinList = [500, 100, 50, 10]
result = 0

for coin in coinList:
  result += n // coin
  n %= coin
  
print(result)