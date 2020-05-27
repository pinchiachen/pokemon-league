// 2020/02/18
var countBinarySubstrings = function(s) {
  let arr = [];
  let curLen = 1;
  let res = 0;
  for (let i = 0; i < s.length - 1; i++) {
    if (s.charAt(i) === s.charAt(i + 1)) {
      curLen += 1;
    } else {
      arr.push(curLen);
      curLen = 1;
    };
  };
  arr.push(curLen);
  for (let i  = 0; i < arr.length - 1; i++) {
    res += Math.min(arr[i], arr[i+1]);
  };
  return res;
};