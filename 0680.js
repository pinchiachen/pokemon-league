// 2020/01/29
var validPalindrome = function(s) {
  let left = 0;
  let right = s.length - 1;
  let list = Array.from(s);
  while (left < right) {
    if (list[left] !== list[right]) {
      let deleteLeft = list.slice(0, left).concat(list.slice(left + 1, list.length));
      let deleteRight = list.slice(0, right).concat(list.slice(right + 1, list.length));
      return (isPalindrome(deleteLeft) == true || isPalindrome(deleteRight) == true) ? true : false
    } else {
      left += 1;
      right -= 1;
    };
  };
  return true
};

var isPalindrome = function(array) {
  let left = 0;
  let right = array.length - 1;
  while (array[left] === array[right] && left < right) {
    left += 1;
    right -= 1;
  };
  return (left - right >= 0) ? true : false;
};