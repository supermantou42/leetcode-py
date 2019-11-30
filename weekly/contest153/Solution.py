from typing import *


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            tmp = start
            start = destination
            destination = tmp
        total = sum(distance)
        dis = sum(distance[start:destination])
        return min(dis, total - dis)

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        m = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if month in [1, 2]:
            month += 12
            year -= 1
        w = int(day + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
        return m[w]

    def maximumSum(self, arr: List[int]) -> int:
        # k = []
        # kl = []
        # s = 0
        # m = 0
        # mm = 0
        # for a in arr:
        #
        #     if s + a < 0:
        #         if s > 0:
        #             k.append(s)
        #             kl.append(mm)
        #         k.append(a)
        #         kl.append(a)
        #         s = 0
        #         mm = 0
        #     else:
        #         s += a
        #         if s > mm:
        #             mm = s
        #         if mm > m:
        #             m = mm
        # if s >= 0:
        #     if s > m:
        #         m = s
        #     k.append(s)
        #     kl.append(mm)
        # if m <= 0:
        #     return max(arr)
        # else:
        #     ans = kl[0]
        #     for i in range(len(k))[1:-1]:
        #         if k[i] < 0:
        #             if k[i - 1] > 0 and kl[i + 1] > 0:
        #                 ans = max(ans, k[i - 1] + kl[i + 1])
        #     return max(ans, kl[-1])
        #
        # s = 0
        # m = 0
        # dif = 0
        # lastindex = 0
        # l = len(arr)
        # i = 0
        # while i < l:
        #     a = arr[i]
        #     nexti = i + 1
        #     if s + a < dif and (a >= dif or s <= 0):
        #         s = 0
        #         dif = 0
        #         nexti = lastindex + 1
        #     else:
        #         if a < dif:
        #             dif = a
        #             lastindex = i
        #         s += a
        #         if s - dif > m:
        #             m = s - dif
        #     i += nexti
        # if s >= dif and s - dif > m:
        #     m = s - dif
        # if m > 0:
        #     return m
        # else:
        #     return max(arr)

        sl = []
        s = 0
        arr.append(-1)
        for a in arr:
            if a < 0:
                if s > 0:
                    sl.append(s)
                sl.append(a)
                s = 0
            else:
                s += a
        ans = sl[0]
        for i in range(len(sl))[1:-1]:
            if sl[i] < 0 and sl[i-1] > 0 and sl[i+1] > 0:
                ans = max(ans, sl[i-1]+sl[i+1])
        return max(ans,max(sl[:-1]))

if __name__ == '__main__':
    s = Solution()
    # print(s.maximumSum([-50]))
    print(s.maximumSum([8,-1,6,-7,-4,5,-4,7,-6]))
    # print(s.maximumSum([1,-2,0,3]))
    # print(s.maximumSum([1,-2,-2,3]))
    # print(s.maximumSum([2,1,-2,-5,-2]))
    # print(s.maximumSum([-1,-1,-1,-1]))
    # print(s.maximumSum([0,-5,-6,5,0,-5]))
    # print(s.maximumSum([1,-4,-5,-2,5,0,-1,2]))
    # print(s.maximumSum([11,-10,-11,8,7,-6,9,4,11,6,5,0]))
    # print(s.maximumSum([-7,6,1,2,1,4,-1]))

    # print(s.maximumSum([11,-10,-11,15,-6,35]))
