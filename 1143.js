// 2020/02/23
var longestCommonSubsequence = function(text1, text2) {
  let n1 = text1.length;
  let n2 = text2.length;
  let dp = new Array(n1 + 1);
  for (let i = 0; i < dp.length; i++) {
      dp[i] = new Array(n2 + 1).fill(0);
  };
  for (let i = 1; i < n1 + 1; i++) {
      for (let j = 1; j < n2 + 1; j++) {
          if (text1.charAt(i - 1) === text2.charAt(j - 1)) {
              dp[i][j] = dp[i - 1][j - 1] + 1;
          } else {
              dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
          };
      };
  };
  return dp[n1][n2];
};