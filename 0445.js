// 2020/02/14
var addTwoNumbers = function(l1, l2) {
  let stack1 = [];
  let stack2 = [];
  let sum = 0;
  let res = null;
  let temp = 0;
  let head;
  while (l1) {
    stack1.push(l1.val);
    l1 = l1.next;
  };
  while (l2) {
    stack2.push(l2.val);
    l2 = l2.next;
  };
  while (stack1.length > 0 || stack2.length > 0 || temp > 0) {
    if (stack1.length > 0) sum += stack1.pop();
    if (stack2.length > 0) sum += stack2.pop();
    sum += temp;
    head = new ListNode(sum % 10);
    head.next = res;
    res = head;
    temp = (sum >= 10) ? 1 : 0;
    sum = 0;
  };
  return head;
};