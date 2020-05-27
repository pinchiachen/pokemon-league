// 2020/02/22
var wiggleMaxLength = function(nums) {
  if (nums.length === 0) return 0;
  let plus = 1;
  let minus = 1;
  for (let i = 1; i < nums.length; i++) {
      if (nums[i] > nums[i - 1]) {
          plus = minus + 1;
      } else if (nums[i] < nums[i - 1]) {
          minus = plus + 1;
      };
  };
  return Math.max(plus, minus);
};