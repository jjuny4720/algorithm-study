def solution(s):
    answer = ''
    count = 1
    
    for i in range(1, len(s)//2 + 1):
        arr = s[0:i]
        print(arr)
        for j in range(len(s)):
            if (arr == s[j:i]):
                count += 1
            else: 
                if(count > 1):
                    answer += str(count)
                    arr = s[j:i]
                    count = 1
        if count > 1:
            answer += str(count)
            answer += arr
 
            
    print(answer)
    print(len(answer))
    
    return len(answer)

s = "aabbaccc"
solution(s)
