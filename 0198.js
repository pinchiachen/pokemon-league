// 2020/02/18
var rob = function(nums) {
  if (nums.length === 0) return 0;
  let pre1 = 0;
  let pre2 = 0;
  let tmp;
  for (let i = 0; i < nums.length; i++) {
    tmp = Math.max(pre2 + nums[i], pre1);
    pre2 = pre1;
    pre1 = tmp;
  };
  return tmp;
};