function binarysearch(target, arr) {
  let answer = "no";
  arr.sort((a, b) => a - b);
  let lt = 0, rt = arr.length - 1;
  while (lt <= rt) {
    let mid = parseInt((lt + rt) / 2);
    if (arr[mid] === target) {
      answer = "yes"
      break;
    } else if (arr[mid] > target) {
      rt = mid - 1;
    } else lt = mid + 1;
  }
  return answer;
}
console.log(buy.map(item => binarysearch(item, sell)));