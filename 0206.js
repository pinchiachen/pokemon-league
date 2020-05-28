// 2020/02/10
var reverseList = function(head) {
  if (!head) return null;
  if (!head.next) return head;
  let cur = head;
  let pre = null;
  let temp;
  while (cur) {
    temp = cur;
    cur = cur.next;
    temp.next = pre;
    pre = temp;
  };
  return pre;
};