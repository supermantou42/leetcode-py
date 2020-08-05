from typing import *
import time

'''
1 两数之和   	47.5%	简单	
2 两数相加   	36.5%	中等	
3 无重复字符的最长子串   	32.7%	中等	
4 寻找两个有序数组的中位数   	36.7%	困难	
5 最长回文子串   	28.3%	中等	
10 正则表达式匹配   	25.8%	困难	
11 盛最多水的容器   	60.9%	中等	
15 三数之和   	25.3%	中等	
17 电话号码的字母组合   	52.2%	中等	
19 删除链表的倒数第N个节点   	37.3%	中等	
20 有效的括号   	40.7%	简单	

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays(nums1 = [1, 3], nums2 = [2]))
    print(s.findMedianSortedArrays(nums1 = [1, 2], nums2 = [3,4]))
    print(s.findMedianSortedArrays(nums1 = [1, 3], nums2 = [2,4]))
    print(s.findMedianSortedArrays(nums1 = [1, 3, 5], nums2 = [2,4]))
    print(s.findMedianSortedArrays(nums1 = [1, 3, 5], nums2 = [2,4,6]))
    print(s.findMedianSortedArrays(nums1 = [1, 2, 3], nums2 = [4,5,6]))
    print(s.findMedianSortedArrays(nums1 = [1, 2, 3], nums2 = [4]))
    print(s.findMedianSortedArrays(nums1 = [1, 3, 4], nums2 = [2]))
    print(s.findMedianSortedArrays(nums1 = [1, 3, 4, 5, 6], nums2 = [2]))