// 2020/02/12
var swapPairs = function(head) {
  let node = new ListNode(0);
  node.next = head;
  let pre = node;
  let cur = head;
  let nextStage;
  while (cur && cur.next) {
      nextStage = cur.next.next;
      cur.next.next = cur;
      pre.next = cur.next;
      cur.next = nextStage;
      pre = cur;
      cur = cur.next;
  };
  return node.next;
};