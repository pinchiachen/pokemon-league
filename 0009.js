// 2020/02/17
var isPalindrome = function(x) {
  if (x < 0) return false;
  if (x < 10) return true;
  let arr = [];
  while (x > 0) {
    arr.push(x % 10);
    x = Math.floor(x / 10);
  };
  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
    if (arr[i] !== arr[arr.length - i - 1]) return false
  };
  return true;
};