from typing import *

class Solution:
    def firstUniqChar(self, s: str) -> str:
        s = [ord(ss) for ss in s]
        vmap = [0]*256
        for ss in s:
            vmap[ss]+=1
        ans = ' '
        for ss in s:
            if vmap[ss] == 1:
                ans = chr(ss)
                break
        return ans

    def reversePairs(self, nums: List[int]) -> int:
        # 插入排序 超时
        # ans = 0
        # n = len(nums)
        # def insert(i,j):
        #     tmp = nums[j]
        #     for ii in range(j,i,-1):
        #         nums[ii] = nums[ii-1]
        #     nums[i] = tmp
        #
        # def binarysearch(right,value):
        #     left = 0
        #     while left < right:
        #         mid = (left+right)//2
        #         if value >= nums[mid]:
        #             left = mid+1
        #         else:
        #             right = mid
        #     return left
        #
        # for i in range(1,n):
        #     pos = binarysearch(i,nums[i])
        #     ans += i-pos
        #     insert(pos,i)
        # return ans
        # 归并排序
        n = len(nums)
        ans = [0]
        sorted_nums = [0]*n
        def merge(l,r):
            if l + 1 >= r:
                return
            mid = (l+r)//2
            merge(l,mid)
            merge(mid,r)
            i,j,k = l,mid,l
            while i < mid and j < r:
                if nums[i] <= nums[j]:
                    sorted_nums[k] = nums[i]
                    ans[0]+=j-mid
                    i+=1
                else:
                    sorted_nums[k] = nums[j]
                    j+=1
                k+=1
            while i < mid:
                sorted_nums[k] = nums[i]
                ans[0] += j - mid
                i += 1
                k+=1

            nums[l:j] = sorted_nums[l:j]
        merge(0,n)
        return ans[0]
        # 离散化树状数组 daily/July.py#line:307:countSmaller


if __name__ == '__main__':
    s = Solution()
    # print(s.firstUniqChar("leetcode"))
    print(s.reversePairs([2, 10, 8, 6, 11, 7, 3, 9, 0, 1, 5, 4]))