# numbers = [6, 10, 2]
# max = 0
# answer = ''

# for number in numbers:
#     if len(str(number)) == 1:
#         if max<number:
#           max = number
#     elif len(str(number)) == 2:
#         if max<number%10:
#           max = number
        
#     elif len(str(number)) == 3:
#         if max<number%100:
#           max = number
#     else:
#         if max<number%1000:
#           max = number

# print(max)
# numbers.remove(max)
# answer += str(max)
# max = 0
# print(numbers, answer)

# for number in numbers:
#     if len(str(number)) == 1:
#         if max<number:
#           max = number
#     elif len(str(number)) == 2:
#         if max<number%10:
#           max = number
        
#     elif len(str(number)) == 3:
#         if max<number%100:
#           max = number
#     else:
#         if max<number%1000:
#           max = number

# print(max)
# numbers.remove(max)
# answer += str(max)
# max = 0
# print(numbers, answer)

numbers = [3, 30, 34, 5, 9]

def solution(numbers):
  answer = ''
  numbers_list = [str(number) for number in numbers]
  numbers_list.sort(key=lambda number:number*3, reverse=True)
  answer = str(int(''.join(numbers_list)))
  return answer

print(solution(numbers))
