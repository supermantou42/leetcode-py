from typing import *
import time


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        aset = set(arr2)
        cnt = 0
        for a in arr1:
            if a in aset:
                continue
            flag = True
            for i in range(d):
                if a + i + 1 in aset or a - i - 1 in aset:
                    flag = False
                    break
            if flag:
                cnt += 1
        return cnt

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        cnt = 2 * n
        reservedSeats.sort(key=lambda x: x[0])
        reservedSeats.append([n + 1, -1])
        rt = []
        last = -1
        for rs in reservedSeats:
            if rs[0] > last:
                if rt:
                    srt = set(rt)
                    if len({2, 3, 4, 5} & srt) > 0 and len({6, 7, 8, 9} & srt) > 0 and len({4, 5, 6, 7} & srt) > 0:
                        cnt -= 2
                    else:
                        cnt -= 1

                rt = []
                last = rs[0]

            if 1 < rs[1] < 10:
                rt.append(rs[1])

        return cnt

    def getKth(self, lo: int, hi: int, k: int) -> int:
        # from queue import PriorityQueue
        vmap = {1: 0}

        def gett(x):
            if x in vmap:
                return vmap[x]
            if x % 2 == 0:
                y = gett(x // 2) + 1
            else:
                y = gett(3 * x + 1) + 1
            vmap[x] = y
            return y

        # pq = PriorityQueue()
        arr = list(range(lo, hi + 1))
        for i in arr:
            gett(i)
        arr.sort(key=lambda x: vmap[x])
        return arr[k - 1]
        #     pq.put_nowait(gett(i))
        #     if pq.qsize() > k:
        #         pq.get_nowait()
        # while pq.qsize() > 1:
        #     pq.get_nowait()
        # return pq.get_nowait()

    def maxSizeSlices(self, slices: List[int]) -> int:
        '''
        给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：

        你挑选 任意 一块披萨。
        Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
        Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
        重复上述过程直到没有披萨剩下。
        每一块披萨的大小按顺时针方向由循环数组 slices 表示。

        请你返回你可以获得的披萨大小总和的最大值。
        :param slices:
        :return:
        示例 1：
        输入：slices = [1,2,3,4,5,6]
        输出：10
        解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
        输入：slices = [8,9,8,6,1,1]
        输出：16
        解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
        示例 3：

        输入：slices = [4,1,2,5,8,3,1,9,7]
        输出：21
        示例 4：

        输入：slices = [3,1,2]
        输出：3
        '''
        # n = len(slices) // 3
        # cnt = 0
        # for _ in range(n):
        #     pick = 0
        #     gain = slices[0] - slices[1] - slices[-1]
        #     for i in range(1,len(slices)-1):
        #         if slices[i] - slices[i+1] - slices[i-1] > gain:
        #             pick = i
        #             gain = slices[i] - slices[i+1] - slices[i-1]
        #     if slices[-1] - slices[0] - slices[-2] > gain:
        #         cnt += slices[-1]
        #         slices = slices[1:-2]
        #     else:
        #         cnt += slices[pick]
        #         if pick == 0:
        #             slices = slices[2:-1]
        #         else:
        #             slices = slices[:pick-1] + slices[pick+2:]
        # return cnt
        n = len(slices)
        cnt = [0]

        def dfs(deep, t, v, picked):

            if deep == n:
                cnt[0] = max(cnt[0], v)
                return
            if len(picked) > 0:
                if deep - picked[-1] > 1 and t > 0:
                    dfs(deep + 1, t - 1, v + slices[deep], picked + [deep])
            elif t > 0:
                dfs(deep + 1, t - 1, v + slices[deep], picked + [deep])
            dfs(deep + 1, t, v, picked)

        dfs(0, n // 3, 0, [])
        return cnt[0]


if __name__ == '__main__':
    s = Solution()
    # print(s.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
    # print(s.maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
    # print(s.maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
    # print(s.maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))
    # print(s.maxNumberOfFamilies(2,
    #                             [[1, 6], [1, 8], [1, 3], [2, 3], [1, 10], [1, 2], [1, 5], [2, 2], [2, 4], [2, 10],
    #                              [1, 7], [2, 5]]))
    # print(s.getKth(lo = 12, hi = 15, k = 2))
    # print(s.getKth(lo = 1, hi = 1, k = 1))
    # print(s.getKth(lo = 7, hi = 11, k = 4))
    # print(s.getKth(lo = 10, hi = 20, k = 5))
    # print(s.getKth(lo = 1, hi = 1000, k = 777))
    print(s.maxSizeSlices([1, 2, 3, 4, 5, 6]))
    print(s.maxSizeSlices([8, 9, 8, 6, 1, 1]))
    print(s.maxSizeSlices([4, 1, 2, 5, 8, 3, 1, 9, 7]))
    print(s.maxSizeSlices([3, 1, 2]))
    print(s.maxSizeSlices([4, 2, 9, 3, 4, 7]))
