from typing import *
import time

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        import collections
        c = collections.Counter(arr)
        ans = -1
        for k,v in c.items():
            if k == v:
                ans = max(ans,k)
        return ans

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for _ in range(2):
            dp = [0]*n
            for i in range(1,n):
                k = 0
                for t in rating[:i]:
                    if rating[i] > t:
                        k += 1
                dp[i] = k
            total = 0
            for i in range(2,n):
                for j,t in enumerate(rating[:i]):
                    if rating[i] > t:
                        total += dp[j]
            ans += total
            rating.reverse()
        return ans

class UndergroundSystem:

    def __init__(self):
        self.stationNamemap = {}
        # self.time_ret = []
        self.id_checkin = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.stationNamemap:
            self.stationNamemap[stationName] = {}
        self.id_checkin[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time,start = self.id_checkin[id]
        time = t - time
        fromstation = self.stationNamemap[start]
        if stationName not in fromstation:
            fromstation[stationName] = [time,1]
        else:
            fromstation[stationName][0] += time
            fromstation[stationName][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        try:
            total,n = self.stationNamemap[startStation][endStation]
            return total/n
        except:
            return 0.


def uddebuger(method,arg):

    ud = UndergroundSystem()
    n = len(method)
    for i in range(1,n):
        m = method[i]
        a = arg[i]
        if m == 'checkIn':
            ud.checkIn(a[0],a[1],a[2])
        elif m == 'checkOut':
            ud.checkOut(a[0],a[1],a[2])
        else:
            print(ud.getAverageTime(a[0], a[1]))
            # ud.getAverageTime(a[0], a[1])

if __name__ == '__main__':
    s = Solution()
    # print(s.numTeams(rating = [2,5,3,4,1]))
    # print(s.numTeams(rating = [2,1,3]))
    # print(s.numTeams(rating = [1,2,3,4]))
    uddebuger(["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
,[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
)
    # import json
    # f = open('data.json')
    # j = json.load(f)
    # start = time.time()
    # uddebuger(j['method'],j['args'])
    # print(time.time()-start)



