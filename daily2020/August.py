from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1st
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        heap = []
        maxv = nums[0][0]
        for i in range(len(nums)):
            maxv = max(maxv,nums[i][0])
            heap.append([nums[i][0],i,0])
        heapq.heapify(heap)
        ans = [heap[0][0],maxv]

        while True:
            v = heapq.heappop(heap)
            if v[2] == len(nums[v[1]]) - 1:
                return ans
            maxv = max(maxv,nums[v[1]][v[2]+1])
            heapq.heappush(heap,[nums[v[1]][v[2]+1],v[1],v[2]+1])
            if maxv - heap[0][0] < ans[1] - ans[0]:
                ans = [heap[0][0],maxv]
        return ans
    #2nd
    def flatten(self, root: TreeNode) -> None:
        self.now_node = root
        def preorder(node: TreeNode):
            if node is None:
                return
            r = node.right
            self.now_node.left = None
            self.now_node.right = node
            self.now_node = node
            preorder(node.left)
            preorder(r)
        if root:
            r = root.right
            preorder(root.left)
            preorder(r)

    #3rd
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if n1 > n2:
            num2 = '0'*(n1-n2)+num2
        else:
            num1 = '0'*(n2-n1)+num1
        c = 0
        ans = ''
        base = ord('0')
        for i in range(max(n1,n2)-1,-1,-1):
            d = ord(num1[i]) + ord(num2[i]) + c - 2*base
            c = 0 if d < 10 else 1
            ans+=str(d%10)
        if c == 1:
            ans += '1'
        return ans[::-1]

    # 4th
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        in_degree = [0] * numCourses
        visited = [False] * numCourses
        edges = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            in_degree[edge[1]]+=1
            edges[edge[0]].append(edge[1])
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        while q:
            e = q.popleft()
            visited[e] = True
            for nexte in edges[e]:
                if visited[nexte]:
                    return False
                in_degree[nexte] -= 1
                if in_degree[nexte] == 0:
                    q.append(nexte)
        return sum(visited) == numCourses

    # 5th
    def rob(self, root: TreeNode) -> int:

        def postorder(node: TreeNode):
            if node is None:
                return 0,0
            l1,l2 = postorder(node.left)
            r1,r2 = postorder(node.right)
            a1 = node.val + l2 + r2
            a2 = max(l1,l2)+max(r1,r2)
            return a1,a2
        return max(postorder(root))




if __name__ == '__main__':
    s = Solution()
    # print(s.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(6)
    # s.flatten(root)
    # print(s.addStrings('9','99'))
    print(s.canFinish(2,[[1,0]]))
    print(s.canFinish(2,[[1,0],[0,1]]))