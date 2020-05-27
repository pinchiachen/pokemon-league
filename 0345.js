// 2020/01/21
var reverseVowels = function(s) {
  let left = 0;
  let right = s.length - 1;
  let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let arr = Array.from(s);
  while (left < right) { 
    if (!vowels.includes(arr[left])) {
          left += 1;
      };
    if (!vowels.includes(arr[right])) {
        right -= 1;
    };
    if ((vowels.includes(arr[left]) && vowels.includes(arr[right]))) {   
      let tmp = arr[left];
      arr[left] = arr[right];
      arr[right] = tmp;
      left += 1;
      right -= 1;
    };
  };
  return arr.join('');
};