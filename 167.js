// 2020/01/20
var twoSum = function(numbers, target) {
  let dict = {};
  for (let i=0; i<numbers.length; i++) {
      if (target - numbers[i] in dict) {
          return ([dict[target-numbers[i]], i+1])
      } else {
          dict[numbers[i]] = i+1;
      }
  }
};