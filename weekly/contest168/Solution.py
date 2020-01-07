from typing import *
import time
import collections
# import line_profiler_py35

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                cnt+=1
        return cnt


    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # s = collections.Counter(nums)
        # ordered_nums = sorted(s)
        # for num in ordered_nums:
        #     occ = s[num]
        #     if s[num] > 0:
        #         for i in range(num + 1, num + k):
        #             if s[i] >= occ:
        #                 s[i] -= occ
        #             else:
        #                 return False
        # return True

        total = len(nums)
        if total % k > 0:
            return False
        min_num = min(nums)
        max_num = max(nums)
        nmap = [0] * (max_num - min_num + 1)
        tn = list(set(nums))
        tn.sort()
        for n in nums:
            nmap[n - min_num] += 1

        for last in tn:
            last = last - min_num
            if nmap[last] > 0:
                if last + k > max_num - min_num + 1:
                    return False
                n = nmap[last]
                for i in range(last,last+k):
                    if nmap[i] < n:
                        return False
                    nmap[i] -= n
        return True

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = len(s)
        d = [-1] * l
        letters_cnt = [0]*26
        ord_a = ord('a')
        base = 0
        let_n = 0
        for i in range(minSize):
            vi = ord(s[i]) - ord_a
            base = base*26 + vi
            if letters_cnt[vi] == 0:
                let_n += 1
            letters_cnt[vi]+=1
        if let_n <= maxLetters:
            d[minSize-1] = base
        lbase = (26**(minSize-1))
        for i in range(minSize,l):
            vim = ord(s[i-minSize]) - ord_a
            vi = ord(s[i]) - ord_a
            base = (base - vim * lbase)*26 +vi

            if letters_cnt[vi] == 0:
                let_n += 1
            letters_cnt[vi]+=1
            letters_cnt[vim] -= 1
            if letters_cnt[vim] == 0:
                let_n -= 1

            if let_n <= maxLetters:
                d[i] = base
            else:
                d[i] = -1
        import collections
        count = collections.Counter(d)
        count[-1] = 0
        return max(count.values())

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        all_keys=[]
        all_boxes=[]
        all_candy = 0
        for b in initialBoxes:
            if status[b] == 1:
                all_keys += keys[b]
                all_boxes += containedBoxes[b]
                all_candy += candies[b]
            else:
                all_boxes.append(b)
        for i in range(n):
            if status[i] == 1:
                all_keys.append(i)
        all_keys = list(set(all_keys))

        while True:
            more = 0
            for b in all_boxes.copy():
                if b in all_keys:
                    all_keys.remove(b)
                    all_keys += keys[b]

                    all_boxes.remove(b)
                    all_boxes += containedBoxes[b]
                    more += candies[b]

            if more == 0:
                break
            all_candy += more
        return all_candy

if __name__ == '__main__':
    s = Solution()
    # with open('./data.txt','r') as f:
    #     data = f.readlines()
    #     data = list(map(lambda x:int(x.strip()),data))

    print(s.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
    print(s.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))
    print(s.maxFreq(s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3))
    print(s.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3))

    # st = time.time()
    # print(s.isPossibleDivide(data,50000))
# 50000))
#     print(s.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
#     print(s.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
#     print(s.maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]))
#     print(s.maxCandies(status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []))
#     print(s.maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]))
#     print(s.maxCandies([1,0,0,0],
# [1,2,3,4],
# [[1,2],[3],[],[]],
# [[2],[3],[1],[]],
# [0]))
#     print(time.time() - st)