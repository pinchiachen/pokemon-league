// 2020/02/11
var removeNthFromEnd = function(head, n) {
  let node = new ListNode(0);
  node.next = head;
  let slow = node;
  let fast = head;
  while (n > 0) {
      fast = fast.next;
      n -= 1;
  };
  while (fast) {
      fast = fast.next;
      slow = slow.next;
  };
  if (slow.next === null) {
      slow.next = null;
  } else {
      slow.next = slow.next.next;
  };
  return node.next;
};