function solution(input) {
  let arr = input.split("");
  let alph = [];
  let sum = 0;
  arr.forEach((s) => {
    if (s.match(/[A-Z]/gi)) alph.push(s);
    else sum += Number(s);
  });
  return alph.sort().join("") + sum;
}

//test
console.log(solution("K1KA5CB7")); 