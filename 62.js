// 2020/02/19
var uniquePaths = function(m, n) {
  let arr = Array(n).fill(Array(m).fill(1));
  for (let i = 1; i < n; i++) {
    for (let j = 1; j < m; j++) {
      arr[i][j] = arr[i-1][j] + arr[i][j-1];
    };
  };
  return arr[n-1][m-1];
};