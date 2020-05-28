// 2020/02/17
var countSubstrings = function(s) {
  let res = 0;
  for (let i = 0; i < s.length; i++) {
    res += countPalindromic(s, i, i);
    res += countPalindromic(s, i, i + 1);
  };
  return res;
};

var countPalindromic = function(s, start, end) {
  let count = 0;
  while (start >= 0 && end < s.length && s.charAt(start) === s.charAt(end)) {
    start -= 1;
    end += 1;
    count += 1;
  };
  return count;
};