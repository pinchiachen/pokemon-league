// 2020/02/24
var canPartition = function(nums) {
  let sum = 0;
  for (let i of nums) {
    sum += i;
  };
  if (sum % 2 !== 0) return false;
  let W = sum / 2;
  let dp = new Array(W + 1).fill(false);
  dp[0] = true;
  for (let i = 0; i < nums.length; i++) {
    for (let j = W; j >= nums[i]; j--) {
      dp[j] = dp[j] || dp[j - nums[i]];
    };
  };
  return dp[W];
};