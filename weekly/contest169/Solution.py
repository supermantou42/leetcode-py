from typing import *
import time


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 1:
            ans.append(0)
        for i in range(n // 2):
            ans.append((i + 1))
            ans.append(-(i + 1))
        return ans

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        vals = []

        def go(node):
            if node is not None:
                vals.append(node.val)
                go(node.left)
                go(node.right)

        go(root1)
        go(root2)
        vals.sort()
        return vals

    def canReach(self, arr: List[int], start: int) -> bool:
        import queue
        n = len(arr)
        q = queue.Queue()
        q.put_nowait(start)
        visited = set()
        visited.add(start)
        while not q.empty():
            for _ in range(q.qsize()):
                p = q.get_nowait()
                if arr[p] == 0:
                    return True
                l = p - arr[p]
                r = p + arr[p]
                if l >= 0 and l not in visited:
                    visited.add(l)
                    q.put_nowait(l)
                if r < n and r not in visited:
                    visited.add(r)
                    q.put_nowait(r)
        return False

    # https://leetcode-cn.com/problems/verbal-arithmetic-puzzle/solution/dfsjian-zhi-python-80ms-by-yi-lou-ting-feng-2/
    def isSolvable(self, words: List[str], result: str) -> bool:
        from collections import defaultdict
        letter_dict = defaultdict(int)
        not_zero_letter_set = set()
        for word in words:
            not_zero_letter_set.add(word[0])
            for i, letter in enumerate(word[::-1]):
                letter_dict[letter] += 10 ** i
        not_zero_letter_set.add(result[0])
        for i, letter in enumerate(result[::-1]):
            letter_dict[letter] -= 10 ** i
        arr = sorted(letter_dict.values(), key=lambda x: abs(x), reverse=True)
        not_zero_idx_set = {arr.index(letter_dict[letter]) for letter in not_zero_letter_set}

        length = len(arr)
        flag_num = [True] * 10

        def dfs(i, s):
            if i == length:
                if s == 0:
                    return True
                return False
            # 剪枝
            for num in range(10)[::-1]:
                if flag_num[num]:
                    if num * sum([arr[j] for j in range(i, length) if arr[j] > 0]) + s < 0 or \
                            num * sum([arr[j] for j in range(i, length) if arr[j] < 0]) + s > 0:
                        return False
                    break
            for num in range(10)[::-1]:
                if not flag_num[num] or (i in not_zero_idx_set and num == 0):
                    continue
                flag_num[num] = False
                if dfs(i + 1, s + arr[i] * num):
                    return True
                flag_num[num] = True
            return False

        return dfs(0, 0)


if __name__ == '__main__':
    s = Solution()
    # print(s.canReach(arr = [4,2,3,0,3,1,2], start = 5))
    # print(s.canReach(arr = [4,2,3,0,3,1,2], start = 0))
    # print(s.canReach(arr = [3,0,2,1,2], start = 2))
    print(s.isSolvable(words=["SEND", "MORE"], result="MONEY"))
    print(s.isSolvable(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY"))
    print(s.isSolvable(words=["THIS", "IS", "TOO"], result="FUNNY"))
    print(s.isSolvable(words=["LEET", "CODE"], result="POINT"))
