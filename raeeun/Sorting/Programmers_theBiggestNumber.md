# 문제 설명
---
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
<br>
## 제한 사항
---
+ numbers의 길이는 1 이상 100,000 이하입니다.
+ numbers의 원소는 0 이상 1,000 이하입니다.
+ 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

<br>

## 입출력 예
---
|numbers|return|
|---|---|
|[6, 10, 2]|"6210"|
|[3, 30, 34, 5, 9]|	"9534330"|

<br>

# 풀이 코드 (Java)
---
```java
	public String solution(int[] numbers) {
        String answer = "";
        
        //int 배열 (numbers) -> String 배열 (arr)
        int arrLength = numbers.length;
        String[] arr = new String[arrLength];
        for(int i=0; i<arrLength; i++) {
        	arr[i] = Integer.toString(numbers[i]);
        }
        
        //정렬 메소드 오버라이딩
		Arrays.sort(arr, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				String s1 = o1+o2;	String s2 = o2+o1;
				return s2.compareTo(s1);
			}
		});
		
		//numbers의 모든 원소가 0일 경우, 000...출력을 막기 위함
        //allZeroCheck로 모든 원소가 0인 경우를 확인함
		boolean allZeroCheck = true;
        StringBuilder sb = new StringBuilder();
		for(int i=0; i<arrLength; i++) {
			if(allZeroCheck == true && arr[i].equals("0") == false) {
				allZeroCheck = false;
			}
			sb.append(arr[i]);
		}
	
		answer = sb.toString();
        //numbers의 모든 원소가 0일 경우, 0을 출력하기 위함
		if(allZeroCheck) {
			answer = "0";
		}
        return answer;
    }
```