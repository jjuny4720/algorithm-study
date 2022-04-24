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
<<<<<<< HEAD
    print(answer)
    
    return answer
=======
    result = ' '.join(map(str, answer))
    print(result)
    
    return result
>>>>>>> 82ff3d0fb9a231da22bbfda3e901e9828530b111

# test case
# K1KA5CB7 → ABCKK13
# AJKDLSI412K4JSJ9D → ADDIJJJKKLSS20
stringReorder()