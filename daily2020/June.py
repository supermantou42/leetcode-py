from typing import *


class Solution:
    # 29th
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        a = nums[:k]
        a.sort()
        for i in range(k,n):
            if nums[i] > a[0]:
                a[0] = nums[i]
                a.sort()
        return a[0]