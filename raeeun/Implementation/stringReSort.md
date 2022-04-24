# 문제
---
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모드 숫자를 더한 값을 이어서 출력합니다. 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
<br>

# 입력
---
첫째 줄에 하나의 문자열 S가 주어집니다. (1≤S의 길이≤10,000)
<br>

# 출력
---
첫째 줄에 문제에서 요구하는 정답을 출력합니다.
<br>

# 문제 요약
> 문자열(문자 + 숫자)이 주어지면 문자는 정렬하고 숫자는 더하여 뒤에 나타내라 
<br>

# 풀이 코드 (Java)
---
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class StringReSort {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
        //문자열 입력 받기
        String input = br.readLine();
		
		int sum = 0;
		for(int i=0; i<input.length(); i++) {
			char ch = input.charAt(i);
			//문자는 sb에 저장
			if(Character.isAlphabetic(ch)) {
				sb.append(ch);
			} 
            //숫자는 합 구하기
			else if(Character.isDigit(ch)) {
				sum += Character.getNumericValue(ch);
			}
		}
		//char[]에 담고 정렬 및 sb 초기화
		char[] output = sb.toString().toCharArray();
		Arrays.sort(output);
		sb.setLength(0);
        
        //sb에 출력값 넣고 + 숫자들의 합 append
		for(char ch : output) {
			sb.append(ch);
		}
		sb.append(sum);
        
		//결과값 출력
		System.out.println(sb.toString().trim());
		
	}

}
```
<br>

# 코드 설명
---
+ 문자열을 입력받는다.
+ 문자 : sb에 저장 후 정렬
+ 숫자 : 합 구하기
+ 문자+숫자 후 출력
<br>

## 예제 1
---
>입력 : K1KA5CB7
출력 : ABCKK13


## 예제 2
---
>입력 : AJKDLSI412K4JSJ9D
출력 : ADDIJJJKKLSS20
