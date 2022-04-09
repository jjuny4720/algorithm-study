function change(n) {
  let count = 0;
  const array = [500, 100, 50, 10];
  
  for(let coin of array) {
      count += Math.floor(n/coin); //동전 개수
      n -= coin*Math.floor(n/coin); // 남은 돈
  }
  
  return count;
}
  console.log(change(1260));