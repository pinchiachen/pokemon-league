// 2020/02/16
var longestPalindrome = function(s) {
  if (s.length === 0) return 0;
  if (s.length === 1) return 1;
  let dict = {};
  let N = 0;
  let res = 0;
  let hasOne = false;
  while (N < s.length) {
    if (!dict.hasOwnProperty(s.charAt(N))) {
      dict[s.charAt(N)] = 1;
    } else {
      dict[s.charAt(N)] += 1;
    };
    N += 1;
  };
  let arrVal = Object.values(dict);
  for (let val of arrVal) {
    if (val > 1) {
      if (val % 2 === 0) {
        res += val;
      } else {
        res += (val - 1);
        hasOne = true;
      }
    } else {
      hasOne = true;
    };
  };
  return hasOne ? res + 1 : res;
};