// 2020/02/22
var findLongestChain = function(pairs) {
  if (pairs.length <= 1) return pairs.length;
  pairs = pairs.sort((a, b) => a[0] - b[0]);
  let dp = Array(pairs.length).fill(1);
  let res = 0
  for (let i = 1; i < dp.length; i++) {
    for (let j = 0; j < i; j++) {
      if (pairs[i][0] > pairs[j][1]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
    res = Math.max(res, dp[i]);
  };
  return res;
};