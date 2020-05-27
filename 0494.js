// 2020/02/26
var findTargetSumWays = function(nums, S) {
  let sum = 0;
  for (let i of nums) sum += i;
  if ((sum + S) % 2 !== 0 || sum < S) return 0;
  let W = (sum + S) / 2;
  let dp = new Array(W + 1).fill(0);
  dp[0] = 1;
  for (let i = 0; i < nums.length; i++) {
      for (let j = W; j - nums[i] >= 0; j--) {
          dp[j] = dp[j] + dp[j - nums[i]];
      };
  };
  return dp[W];
};