// 2020/02/10
var deleteDuplicates = function(head) {
  if (!head) return null;
  let l = new ListNode(0);
  let res = l;
  while (head.next) {
    if (head.val !== head.next.val) {
      l.next = head;
      l = l.next;
    };
    head = head.next;
  };
  l.next = head;
  return res.next;
};