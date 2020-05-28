// 2020/02/19
var NumArray = function(nums) {
  this.arr = Array(nums.length);
  this.arr[0] = nums[0]
  for (let i = 1; i < this.arr.length; i++) {
    this.arr[i] = this.arr[i - 1] + nums[i];
  };
};

NumArray.prototype.sumRange = function (i, j) {
  if (i === 0) return this.arr[j];
  return this.arr[j] - this.arr[i - 1];
};