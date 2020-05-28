// 2020/02/28
var coinChange = function(coins, amount) {
  let dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let coin of coins) {
    for (let i = coin; amount - i >= 0; i++) {
      if (dp[i - coin] !== Infinity) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      };
    };
  };
  return dp[amount] === Infinity ? -1 : dp[amount];
};