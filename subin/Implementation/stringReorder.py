def stringReorder():
    s = input('입력 : ')
    answer = []
    num = 0

    for i in s:
        if i.isdigit():
            num += int(i)
        else:
            answer.append(i)

    answer.sort()
    answer.append(num)
    #print(num)
    result = ' '.join(map(str, answer))
    print(result)
    
    return result

# test case
# K1KA5CB7 → ABCKK13
# AJKDLSI412K4JSJ9D → ADDIJJJKKLSS20
stringReorder()