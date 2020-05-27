// 2020/02/15
var isIsomorphic = function(s, t) {
  if (s.length !== t.length) return false;
  let dictS = {};
  let dictT = {};
  let N = 0;
  while (N < s.length) {
      if (!dictS.hasOwnProperty(s.charAt(N))) {
          dictS[s.charAt(N)] = s.charCodeAt(N) - t.charCodeAt(N);
      } else {
          if (dictS[s.charAt(N)] !== s.charCodeAt(N) - t.charCodeAt(N)) return false;
      }
      if (!dictT.hasOwnProperty(t.charAt(N))) {
          dictT[t.charAt(N)] = t.charCodeAt(N) - s.charCodeAt(N);
      } else {
          if (dictT[t.charAt(N)] !== t.charCodeAt(N) - s.charCodeAt(N)) return false;
      }
      N++;
  };
  return true;
};