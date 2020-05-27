// 2020/02/18
var climbStairs = function(n) {
  if (n <= 2) return n;
  let pre = 1;
  let cur = 2;
  let tmp;
  for (let i = 3; i < n + 1; i++) {
      tmp = cur + pre;
      pre = cur;
      cur = tmp;
  };
  return cur;
};