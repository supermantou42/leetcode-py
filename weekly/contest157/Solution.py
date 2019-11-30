from typing import *
import time


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        s = [0,0]
        for c in chips:
            s[c%2]+=1
        return min(s)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # s = -1
        # for i in range(len(arr)):
        #     if len(arr) - i <= s:
        #         break
        #     ss = 1
        #     aa = arr[i] + difference
        #     for j in range(i+1,len(arr)):
        #         if arr[j] == aa:
        #             aa += difference
        #             ss += 1
        #     if ss > s:
        #         s = ss
        dm = {}
        brr = [0] * len(arr)
        for i in range(len(arr)):
            be = arr[i] - difference
            brr[i] = dm.get(be,0) + 1
            dm[arr[i]] = brr[i]
        ss = max(brr)
        # marked = [False] * len(arr)
        # for j in range(len(arr))[::-1]:
        #     if marked[j]:
        #         continue
        #     if j <= ss:
        #         break
        #     s = 1
        #     i = j
        #     while brr[i] > -1:
        #         s += 1
        #         i = brr[i]
        #         marked[i] = True
        #     if s > ss:
        #         ss = s
        # print(time.time() - st)
        return ss

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubsequence(arr = [1,2,3,4], difference = 1))
    print(s.longestSubsequence(arr = [1,3,5,7], difference = 1))
    print(s.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))
    print(s.longestSubsequence(arr = [3,0,-3,4,-4,7,6], difference = 3))

    # with open('./data.txt','r') as f:
    #     data = f.readlines()
    # data = list(map(int,data))
    # st = time.time()
    # s.longestSubsequence(arr=data,difference=1)
    # print(time.time()-st)