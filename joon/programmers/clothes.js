function solution(clothes) {
  var answer = 1;
  var obj= {}
  clothes.forEach(function(cloth){
      if(cloth[1] in obj) {
         obj[cloth[1]] += 1;
      }else{
          obj[cloth[1]] = 2;
      }
  })
  for(let key in obj) {
      answer *= obj[key];
  }
  return answer -1; //옷을 아예 입지 않은 경우
}

//풀이방법 : obj라는 객체에 clothes를 돌면서 옷의 종류의 key값이 없으면, obj에 {clothes의 종류:2} 추가.
//그리고 key가 있으면 1을 더해주는 방식