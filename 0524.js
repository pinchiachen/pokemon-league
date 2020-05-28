// 2020/02/10
var findLongestWord = function(s, d) {
  let res = '';
  for (str of d) {
    let left = 0;
    let right = 0;
    while (left < s.length) {
      if (s.charAt(left) === str.charAt(right)) { right += 1; }
      left += 1;
    };
    if (right === str.length && str.length > res.length) {
      res = str;
    } else if (right === str.length && str.length === res.length && str < res) {
      res = str;
    }
  };
  return res;
};