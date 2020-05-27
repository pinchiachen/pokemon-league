// 2020/02/20
var rob = function(nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];
  let arr1 = nums.slice(0, nums.length-1);
  let arr2 = nums.slice(1, nums.length);
  let pre1 = 0;
  let cur1 = 0;
  let tmp1;
  let pre2 = 0;
  let cur2 = 0;
  let tmp2;
  for (let i = 0; i < arr1.length; i++) {
      tmp1 = Math.max(pre1 + arr1[i], cur1);
      pre1 = cur1;
      cur1 = tmp1;
      tmp2 = Math.max(pre2 + arr2[i], cur2);
      pre2 = cur2;
      cur2 = tmp2;
  };
  return (cur1 >= cur2) ? cur1 : cur2; 
};