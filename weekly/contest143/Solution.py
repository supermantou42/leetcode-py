from typing import *


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 0
        ans = [0] * num_people
        while candies > 0:
            give = i + 1
            if give >= candies:
                ans[i % num_people] += candies
                return ans
            ans[i % num_people] += give
            candies -= give
            i += 1
        return ans

    def pathInZigZagTree(self, label: int) -> List[int]:
        import math
        level = int(math.log(label, 2))
        if level % 2 == 1:
            high = 2 ** (level + 1) - 1
            low = 2 ** level
            target = high - label + low
        else:
            target = label
        ans = []
        while target > 0:
            ans.append(target)
            target = target // 2
        ans = ans[::-1]
        for i in range(1, level + 1, 2):
            high = 2 ** (i + 1) - 1
            low = 2 ** i
            ans[i] = high - ans[i] + low
        return ans

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        num = len(books)
        min_height = [0] * num
        min_height[-1] = books[-1][1]
        for i in range(num)[-2::-1]:
            min_height[i] = max(min_height[i+1],books[i][1])
        # path = []
        def go(deep, high, remain, total):
            if deep == num:
                # print(path)
                # print(total+high)
                return total + high
            if remain >= books[deep][0]:
                high_ = max(high, books[deep][1])
                # path.append('%d n' % deep)
                tmp = go(deep + 1, high_, remain - books[deep][0], total)
                # path.pop(-1)
                return tmp
            else:
                tmp = 1e9
            if tmp <= total + min_height[deep]:
                return tmp
            # path.append(deep)
            total_ = go(deep + 1, books[deep][1], shelf_width - books[deep][0], total + high)
            # path.pop(-1)
            if tmp < total_:
                total_ = tmp
            return total_

        return go(0, 0, shelf_width, 0)

    # def minHeightShelves2(self, books: List[List[int]], shelf_width: int) -> int:
        # nums = len(books)
        # d = [[0 for _ in range(nums)] for _ in range(nums)]
        # h = [[0 for _ in range(nums)] for _ in range(nums)]
        # for i in range(nums):
        #     d[i][0] = books[i][1]
        #     h[i][0] = books[i][1]
        # for i in range(nums):
        #     for j in range(i+1):
        #         h_ = max(books[j][])


if __name__ == '__main__':
    s = Solution()
    # print(s.distributeCandies(candies = 10, num_people = 1))
    # print(s.pathInZigZagTree(26))
    # print(s.minHeightShelves([[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]],200))
    print(s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]],4))