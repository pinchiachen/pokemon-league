// 2020/01/20
var judgeSquareSum = function(c) {
  if (c < 0) return false;
  let sum;
  let left = 0;
  let right = parseInt(Math.sqrt(c));
  while (left <= right) {
    sum = left ** 2 + right ** 2;
    if (sum === c) {
      return true
    } else if (sum > c) {
      right -= 1;
    } else if (sum < c) {
      left += 1;
    }
  }
  return false
};