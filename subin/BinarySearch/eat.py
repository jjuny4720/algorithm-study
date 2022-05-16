def binarySearch(n):
    start = 0
    end = len(b) - 1
    answer = 0
    
    #print("now ", a)
    
    while start <= end:
        mid = (start + end) // 2
        if b[mid] < n:
            answer = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    return answer

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    #a, b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    answer = 0
    for i in a:
        answer += binarySearch(i)
    print(answer)
        