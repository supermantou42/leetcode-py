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
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 方法1 直接开数组  时空都是O(N)
        nmap = [0] * 100001
        for n in nums:
            if nmap[n] == 1:
                return n
            else:
                nmap[n] = 1
        # return -1

        # 方法2 基数排序  时间O(N**2),空间O(1)
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
            else:
                i += 1
        return -1

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if n == 0 or m == 0 or matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        # # 法1 二分查找 O(n*log(m))
        # l = 0
        # r = n
        # while l < r:
        #     mid = (l+r)//2
        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] < target:
        #         l = mid + 1
        #     else:
        #         r = mid
        # nst = l - 1
        # while nst >= 0 and matrix[nst][-1] >= target:
        #     l = 0
        #     r = m
        #     while l < r:
        #         mid = (l+r)//2
        #         if matrix[nst][mid] == target:
        #             return True
        #         elif matrix[nst][mid] < target:
        #             l = mid +1
        #         else:
        #             r = mid
        #     nst -= 1

        # return False
        # 法2 右上角开始移动 O(n+m)
        x = 0
        y = m-1
        while y >= 0 and x < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False

    def replaceSpace(self, s: str) -> str:
        # one line
        # return s.replace(" ","%20")
        ss = ""
        last = 0
        for i in range(len(s)):
            if s[i] == " ":
                ss+= s[last:i] + "%20"
                last = i+1
        ss += s[last:]
        return ss

    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def go(po,io):
            if len(po) == 0:
                return None
            root = po[0]
            iidx = io.index(root)
            pidx = iidx
            node = TreeNode(root)
            node.left = go(po[1:pidx],io[:iidx])
            node.right = go(po[pidx+1:],io[iidx+1:])
            return node

        return go(preorder,inorder)


if __name__ == '__main__':
    s = Solution()
    print(s.findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))

