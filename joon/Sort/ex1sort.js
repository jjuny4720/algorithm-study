function solution(numbers) { 
  const numbersString = numbers.map((num) => String(num)); //number요소 문자열로 바꿔줌
  numbersString.sort((a,b) => { // b+a숫자와 a+b숫자 비교 후 내림차순
      return parseInt(b+a) - parseInt(a+b);
  })
  const answer = numbersString.join(''); // 만들어진 배열 문자열 정렬
return parseInt(answer).toString(); //tostring 문자열 반환
}

console.log(solution([3,30,301]))