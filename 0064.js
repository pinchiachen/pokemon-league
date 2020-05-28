// 2020/02/19
var minPathSum = function(grid) {
  const n = grid.length;
  const m = grid[0].length;
  let arr = Array(n).fill(Array(m).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i === 0 && j === 0) {
        arr[i][j] = grid[i][j];
      } else if (i === 0) {
        arr[i][j] = arr[i][j - 1] + grid[i][j];
      } else if (j === 0) {
        arr[i][j] = arr[i - 1][j] + grid[i][j];
      } else {
        arr[i][j] = Math.min(arr[i - 1][j], arr[i][j - 1]) + grid[i][j];
      };
    };
  };
  return arr[n - 1][m - 1];
};