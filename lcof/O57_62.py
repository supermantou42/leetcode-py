from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        # vmap = {target - n for n in nums}
        # for n in nums:
        #     if n in vmap:
        #         return [n, target-n]
        # return []
        # table
        # anums = [target - n for n in nums]
        n = len(nums)
        i,j = 0,n-1
        while i<n and j >= 0:
            if nums[i] == target - nums[j]:
                return [nums[i],target-nums[i]]
            elif nums[i] < target - nums[j]:
                i+=1
            else:
                j-=1
        return []

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        n = target // 2 + 1
        l=0
        r=1
        value = 0
        ans = []
        while l +1 < r or r <= n:
            if value == target:
                ans.append(list(range(l,r)))
                value -= l
                l+=1
            elif value < target:
                value+=r
                r+=1
            else:
                value-=l
                l+=1
        return ans

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = ''
        st = 0
        n = len(s)
        for i in range(1,n):
            if s[i] == ' ':
                if s[i-1] != ' ':
                    ans += s[st:i][::-1]
                st = i+1
        if st < n:
            ans+= s[st:][::-1]
        return ans[::-1]

        # return ' '.join(s.strip().split()[::-1])
        # s = list(s)
        # st = 0
        # n = len(s)
        # for i in range(1,n):
        #     if s[i] == ' ':
        #         s[st:i] = s[st:i][::-1]
        #         st=i+1
        # if st < n:
        #     s[st:] = s[st:][::-1]
        # return ''.join(s[::-1])

    def reverseLeftWords(self, s: str, n: int) -> str:
        s= list(s)
        s[:n] = s[:n][::-1]
        s[n:] = s[n:][::-1]
        return ''.join(s[::-1])

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        ans = []
        for i in range(n-k+1):
            ans.append(max(nums[i:i+k]))
        return ans

    def twoSum_(self, n: int) -> List[float]:
        alpha = 6**n
        b = [1]*6
        for i in range(1,n):
            pn = len(b)
            nn = pn + 5
            c = [sum(b[max(j-5,0):j+1]) for j in range(nn//2)]
            if nn % 2 == 0:
                c += c[::-1]
            else:
                c = c + [sum(b[nn//2-5:nn//2+1])] + c[::-1]
            b = c
        for i in range(len(b)):
            b[i] /= alpha
        return b

    def isStraight(self, nums: List[int]) -> bool:
        d = [0]*14
        for n in nums:
            d[n]+=1
            if n>0 and d[n] > 1:
                return False
        if d[0] == 5:
            return True
        flag = 0
        for i in range(1,14):
            if d[i] == 1:
                flag+=1
                if flag == 5:
                    return True
            else:
                if flag>0:
                    if d[0]>0:
                        d[0]-=1
                        flag+=1
                        if flag == 5:
                            return True
                    else:
                        return False
        # if flag+d[0] == 5:
        #     return True
        return True

    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2,n+1):
            f = (m+f)%i
        return f

from collections import deque
class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.max = deque()


    def max_value(self) -> int:
        if self.max:
            return self.max[0]
        return -1


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max and value > self.max[-1]:
            self.max.pop()
        self.max.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        ret = self.queue.popleft()
        if ret == self.max[0]:
            self.max.popleft()
        return ret


if __name__ == '__main__':
    s = Solution()
    # print(s.findContinuousSequence(9))
    # print(s.reverseLeftWords('abcdefg',2))
    # print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
    # mq = MaxQueue()
    # method = [ "push_back", "push_back", "max_value", "pop_front", "max_value"]
    # value = [ [1], [2], [], [], []]
    # for m,v in zip(method,value):
    #     if m == "push_back":
    #         mq.push_back(v[0])
    #     elif m == "max_value":
    #         print(mq.max_value())
    #     else:
    #         print(mq.pop_front())
    print(s.twoSum_(2))