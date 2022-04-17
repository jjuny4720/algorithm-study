import sys

s = sys.stdin.readline().strip()
str_list = []
sum_of_num = 0
# merged_list = []

def divide_list(obj):
  global sum_of_num
  if ord(obj) >= 65 and ord(obj) <=90:
    str_list.append(obj)
  else:
    sum_of_num += int(obj)

def sort_list(str_list):
  str_list.sort()

def merge_list(str_list, sum_of_num):
  # global merged_list
  # merged_list.append(str_list)
  # merged_list.append(sum_of_num)
  str_list.append(sum_of_num)

def main():
  for obj in s:
    divide_list(obj)
  
  sort_list(str_list)
  merge_list(str_list, sum_of_num)
  print(''.join(map(str, str_list)))

if __name__ == '__main__':
  main()

