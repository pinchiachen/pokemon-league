// 2020/02/14
var splitListToParts = function(root, k) {
  let N = 0;
  let res = Array(k).fill(null);
  let cur = root;
  while (cur) {
    N++;
    cur = cur.next;
  };
  cur = root;
  let size = Math.floor(N / k);
  let tempSize;
  let mod = N % k;
  for (let i = 0; i < k && cur; i++) {
    res[i] = cur;
    tempSize = size + ((mod > 0) ? 1 : 0);
    for (let j = 0; j < tempSize - 1; j++) {
      cur = cur.next;
    };
    let nextNode = cur.next;
    cur.next = null;
    cur = nextNode;
    mod -= 1;
  };
  return res;
};