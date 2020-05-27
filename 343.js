// 2020/02/20
var integerBreak = function(n) {
  let dp = Array(n + 1).fill(1);
  for (let i = 3; i < n + 1; i++) {
      for (let j = 1; j < i; j++) {
          dp[i] = Math.max(dp[i], Math.max(j * (i-j), j * dp[i-j]));
      };
  };
  return dp[n];
};