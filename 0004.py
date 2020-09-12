## 2020/09/12
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        target = (len(nums1) + len(nums2)) // 2
        is_odd = (len(nums1) + len(nums2)) % 2 != 0
        if len(nums1) == 0:
            return nums2[target] if is_odd else (nums2[target] + nums2[target - 1]) / 2
        elif len(nums2) == 0:
            return nums1[target] if is_odd else (nums1[target] + nums1[target - 1]) / 2
        merged_arr = []
        left = 0
        right = 0
        while left <= len(nums1) and right <= len(nums2):
            if len(merged_arr) - 1 == target:
                return merged_arr[-1] if is_odd else (merged_arr[-1] + merged_arr[-2]) / 2
            if left == len(nums1):
                merged_arr.append(nums2[right])
                right += 1
            elif right == len(nums2):
                merged_arr.append(nums1[left])
                left += 1
            elif nums2[right] < nums1[left]:
                merged_arr.append(nums2[right])
                right += 1
            elif nums2[right] >= nums1[left]:
                merged_arr.append(nums1[left])
                left += 1

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([2], [1]))