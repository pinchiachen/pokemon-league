// 2020/02/27
var findMaxForm = function(strs, m, n) {
  if (strs.length === 0) return 0;
  let dp = new Array(m + 1);
  for (let i = 0; i < m + 1; i++) {
    dp[i] = new Array(n + 1).fill(0);
  };
  for (let str of strs) {
    let zeros = 0;
    let ones = 0;
    for (let c of str) {
      if (c === '0') {
        zeros += 1;
      } else {
        ones += 1;
      };
    };
    for (let i = m; i - zeros >= 0; i--) {
      for (let j = n; j - ones >= 0; j--) {
        dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
      };
    };
  };
  return dp[m][n];
};