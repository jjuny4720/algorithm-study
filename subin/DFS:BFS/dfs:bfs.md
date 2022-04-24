# 구현 알고리즘 (Implementation Algorithm)

- 구현 문제 유형은 모든 범위의 코딩 테스트 문제 유형을 포함하는 개념
- 파이썬의 경우 자료형의 표현 범위 제한에 대해 깊게 생각하지 않아도 되지만 실수형 변수는 유효숫자에 따라서 연산 결과가 원하는 값이 나오지 않을 수 있음
- 크기가 1,000만 이상인 리스트가 있다면 메모리 용량 제한으로 문제를 풀 수 없게 되는 경우도 있음
- 일반적인 기업 코딩 테스트 환경에서는 파이썬으로 제출한 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하면 크게 무리가 없음
- 알고리즘 문제를 풀 때는 시간제한과 데이터의 개수를 먼저 확인한 뒤에 이 문제를 어느 정도의 시간 복잡도의 알고리즘으로 작성해야 풀 수 있을 것인지 예측할 수 있어야 함

## 문제
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출련한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

### 입력
첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

### 출력
첫째 줄에 문제에서 요구하는 정답을 출력합니다.

```python
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
    print(answer)
    
    return answer

# test case
# K1KA5CB7 → ABCKK13
# AJKDLSI412K4JSJ9D → ADDIJJJKKLSS20
stringReorder()
```

1. for문으로 숫자인 경우 num에 더하고 문자인 경우 answer에 저장 (isdigit함수)
2. 알파벳 순으로 정렬 (sort)
3. 문자열 끝에 숫자 합 넣기