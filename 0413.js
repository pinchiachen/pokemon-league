// 2020/02/19
var numberOfArithmeticSlices = function(A) {
  let dp = Array(A.length).fill(0);
  let res = 0;
  for (let i = 2; i < dp.length; i++) {
      if (A[i] - A[i-1] === A[i-1] - A[i-2]) {
          dp[i] = dp[i-1] + 1;
      };
  };
  for (let i of dp) {
      res += i;
  };
  return res;
};