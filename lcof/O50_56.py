from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 长度对齐
        # n1,n2 = 0,0
        # ha,hb = headA,headB
        # while ha is not None:
        #     n1+=1
        #     ha = ha.next
        # while hb is not None:
        #     n2+=1
        #     hb = hb.next
        # ha,hb = headA,headB
        # if n1 > n2:
        #     for _ in range(n1 - n2):
        #         ha = ha.next
        # else:
        #     for _ in range(n2 - n1):
        #         hb = hb.next
        # if ha == hb:
        #     return ha
        # ans = None
        # while ha is not None:
        #     if ha.next == hb.next:
        #         ans = ha.next
        #         break
        #     ha = ha.next
        #     hb = hb.next
        # return ans
        # 双指针
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        ans = 0
        for i in range(l,len(nums)):
            if nums[i] == target:
                ans+=1
            else:
                break
        return ans

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n
        while l < r:
            mid = (l+r)//2
            if nums[mid] == mid:
                l = mid +1
            else:
                r = mid
        return l

    def kthLargest(self, root: TreeNode, k: int) -> int:

        def midorder(node:TreeNode,k):
            if node is None:
                return 0, None

            right, ans = midorder(node.right,k)
            if ans:
                return 0,ans

            if right + 1 == k:
                return 0,node.val

            left, ans = midorder(node.left,k - right - 1)
            if ans:
                return 0,ans
            return left+right+1,None
        _,ans = midorder(root,k)
        return ans

    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            return max(dfs(node.left),dfs(node.right))+1
        return dfs(root)

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if node is None:
                return 0,True
            l,lf = dfs(node.left)
            r,rf = dfs(node.right)
            if lf and rf and (-1<= r-l <= 1):
                return max(l,r)+1,True
            return max(l,r)+1,False
        return dfs(root)[1]

    def singleNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        v = nums[0]
        for i in range(1,n):
            v ^= nums[i]
        mask = v&(-v)
        ans = [0,0]
        for i in range(n):
            if nums[i] & mask > 0:
                ans[0] ^= nums[i]
            else:
                ans[1] ^= nums[i]
        return ans

    def singleNumber_3(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == '__main__':
    s = Solution()
    # print(s.firstUniqChar("leetcode"))
    # print(s.reversePairs([2, 10, 8, 6, 11, 7, 3, 9, 0, 1, 5, 4]))
    print(s.singleNumbers([4,1,4,6]))
    print(s.singleNumbers([1,2,10,4,1,4,3,3]))