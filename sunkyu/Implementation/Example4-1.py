import sys

n = map(int, sys.stdin.readline())
plan_list = list(map(str, sys.stdin.readline().strip().split(' ')))
position_column = 1
position_row = 1

def move(plan):
  global position_column
  global position_row
  
  if plan == 'L':
    if position_row != 1:
      position_row -= 1
  
  if plan == 'R':
    if position_row != n:
      position_row += 1

  if plan == 'U':
    if position_column != 1:
      position_column -= 1
  
  if plan == 'D':
    if position_column != n:
      position_column += 1

def main():
  for plan in plan_list:
    move(plan)

  print(position_column, position_row)

if __name__ == '__main__':
  main()