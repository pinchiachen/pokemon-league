// 2020/02/20
var integerBreak = function(n) {
  if (n === 2 || n === 3) return n - 1;
  if (n === 4) return 4;
  let res = 1;
  while (n > 4) {
    n -= 3;
    res *= 3;
  };
  res *= n;
  return res;
};