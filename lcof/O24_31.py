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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        next = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        top = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                top.next = l1
                l1 = l1.next
            else:
                top.next = l2
                l2 = l2.next
            top = top.next
        if l1 is not None:
            top.next = l1
        else:
            top.next = l2
        return head

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False

        def checktree(nodeA: TreeNode, nodeB: TreeNode):

            if nodeB is None:
                print('A is ', nodeA)
                return True
            if nodeA is None or nodeA.val != nodeB.val:
                return False
            return checktree(nodeA.left, nodeB.left) and checktree(nodeA.right, nodeB.right)

        def dfs(node):
            if node is None:
                return False
            if node.val == B.val and checktree(node, B):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(A)

    def mirrorTree(self, root: TreeNode) -> TreeNode:

        def inorder(node: TreeNode):
            if node is None:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp
            inorder(node.right)
            inorder(node.left)
            return

        inorder(root)
        return root


    def isSymmetric(self, root: TreeNode) -> bool:
        # BFS
        # if root is None:
        #     return True
        # queue = [root]
        # nextqueue = []
        # flag = True
        # while flag:
        #     flag = False
        #     for q in queue:
        #         if q is None:
        #             nextqueue.append(None)
        #             nextqueue.append(None)
        #         else:
        #             nextqueue.append(q.left)
        #             nextqueue.append(q.right)
        #             flag = True
        #     n = len(nextqueue)
        #     cmp = nextqueue[n//2:][::-1]
        #     for a,b in zip(nextqueue,cmp):
        #         if a is None or b is None:
        #             if a != b:
        #                 return False
        #         elif a.val != b.val:
        #             return False
        #     queue = nextqueue
        #     nextqueue = []
        #
        # return True

        #DFS
        if root is None:
            return True
        def go(A:TreeNode,B:TreeNode):
            if A is None or B is None:
                return A == B
            if A.val != B.val:
                return False
            return go(A.left,B.right) and go(A.right,B.left)
        return go(root,root)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        bm = 0
        bn = 0
        d = 0
        while bm < m or bn < n:
            if d == 0:
                ans += matrix[bm][bn:n]
                d = 1
                bm += 1
            elif d == 1:
                for i in range(bm,m):
                    ans.append(matrix[i][n-1])
                n -= 1
                d = 2
            elif d == 2:
                ans += matrix[m-1][bn:n][::-1]
                d = 3
                m -= 1
            else:
                for i in range(bm,m)[::-1]:
                    ans.append(matrix[i][bn])
                bn += 1
                d = 0
        return ans

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 模拟法
        stack = []
        m,n = len(pushed), len(popped)
        i,j = 0,0

        while j < n:
            # if len(stack) == 0:
            #     return False
            if i == m:
                return stack == popped[j:][::-1]

            stack.append(pushed[i])
            while j < n and popped[j] == stack[-1]:
                j+=1
                if len(stack) == 0:
                    return False
                stack.pop()
                if len(stack) == 0:
                    break
        return True





class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        if len(self.s2) == 0 or self.s2[-1] >= x:
            self.s2.append(x)


    def pop(self) -> None:
        if len(self.s1) == 0:
            return None
        x = self.s1.pop()
        if x == self.s2[-1]:
            self.s2.pop()


    def top(self) -> int:
        if len(self.s1) > 0:
            return self.s1[-1]
        return -1

    def min(self) -> int:
        if len(self.s2) > 0:
            return self.s2[-1]
        return -1


if __name__ == '__main__':

    s = Solution()

    s.validateStackSequences([1,0],[1,0])