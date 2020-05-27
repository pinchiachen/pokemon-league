// 2020/02/14
var isPalindrome = function(head) {
  if (!head) return true;
  let arr = [];
  while (head) {
      arr.push(head.val);
      head = head.next;
  }
  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
      if (arr[i] !== arr[arr.length - i - 1]) return false
  };
  return true;
};