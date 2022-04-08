n = 3
lost = [3]
reserve = [1]

def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for l in set_lost:
      a = l - 1
      b = l + 1

      if a in set_reserve:
        set_reserve.remove(a)
      elif b in set_reserve:
        set_reserve.remove(b)
      else:
        n -= 1

    answer = n
    return answer

solution(n, lost, reserve)