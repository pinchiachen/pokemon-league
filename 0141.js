// 2020/01/29
var hasCycle = function(head) {
  if (head == null) return false;
  let left = head;
  let right = head;
  while (right && right.next) {
    right = right.next.next;
    left = left.next;
    if (left == right) return true;
  };
  return false;
};