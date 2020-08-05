from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            n = n & (n-1)
            cnt += 1
        return cnt

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            sign = -1
            n = -n
        else:
            sign = 1

        ans = 1.
        y = x
        while n > 0:
            if n % 2 == 1:
                ans *= y
                n-=1
            else:
                y *= y
                n //= 2
        if sign == 1:
            return ans
        else:
            return 1/ans

    def printNumbers(self, n: int) -> List[int]:
        base = list(range(10))
        firstbase = base[1:]

        if n == 1:
            return firstbase
        ans = firstbase.copy()
        prev = firstbase.copy()
        while n > 1:
            tmp = []
            for p in prev:
                tmp += [10*p+bb for bb in base]
            prev = tmp.copy()
            ans += tmp
            n-=1
        return ans

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        if head.val == val:
            return head.next
        prev = head
        node = prev.next
        while node is not None:
            if node.val == val:
                prev.next = node.next
                return head
            else:
                prev = node
                node = node.next

        return None

    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            if p[i - 1] == '*':
                if i == 1:
                    dp[0][i] = True
                else:
                    dp[0][i] = dp[0][i - 2]
            # else:
            #     dp[0][i] = False
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if p[i - 1] == '*':
                    dp[j][i] = dp[j][i - 2] or (dp[j - 1][i] and (p[i - 2] == '.' or p[i - 2] == s[j - 1]))
                else:
                    dp[j][i] = dp[j - 1][i - 1] and (p[i - 1] == '.' or p[i - 1] == s[j - 1])

        return dp[-1][-1]

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        if n == 0:
            return False
        if s[0] in ['+','-']:
            if n == 1:
                return False
            s = s[1:]
            n -= 1
        nmap=['%d' % i for i in range(10)]
        Emod = False
        dotmod = False
        novalue = True
        skipnext = False
        for idx,ss in enumerate(s):
            if skipnext:
                skipnext =False
                continue
            if ss == '.':
                if dotmod or Emod:
                    return False
                dotmod = True
                # novalue = True
            elif ss == 'e':
                if Emod or novalue:
                    return False
                if idx + 1 == n:
                    return False
                if s[idx+1] in ['+','-']:
                    skipnext = True
                Emod = True
                novalue = True
                # dotmod = False
            else:
                if ss not in nmap:
                    return False
                novalue = False

        return not novalue

    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        while i < j:
            if nums[i] % 2 == 0:
                if nums[j] % 2 == 1:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    i+=1
                j-=1
            else:
                i += 1
        return nums

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        queue = []
        while head is not None:
            queue.append(head)
            if len(queue) > k:
                queue.pop(0)
            head = head.next
        return queue[0]


if __name__ == '__main__':
    s = Solution()
    # print(s.printNumbers(3))
    print(s.isMatch(s = "mississippi", p = "mis*is*p*."))