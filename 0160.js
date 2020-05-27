// 2020/02/10
var getIntersectionNode = function(headA, headB) {
  let aStart = headA;
  let bStart = headB;
  while (headA !== headB) {
      headA = (headA === null) ? bStart : headA.next;
      headB = (headB === null) ? aStart : headB.next;
  };
  return headA;
};