def solution(s):
    # nonlocal answer
    answer = []
    num_dict = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    
    num = ""
    
    for char in s:

        if char.isdecimal():
            answer.append(char)
            
        else:
            num += char

            for obj in num_dict:
              if obj in num:
                answer.append(num_dict[obj])
                num = num.strip(obj)
    answer = ''.join(answer)
    return int(answer)

s = "one4seveneight"
solution(s)