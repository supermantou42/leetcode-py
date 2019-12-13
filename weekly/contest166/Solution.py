from typing import *
import time


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, list(str(n))))
        a = sum(n)
        b = 1
        for i in n:
            b *= i
        return b - a

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in group:
                group[size] = []
            group[size].append(i)

        ans = []
        for k, v in group.items():
            while len(v) > 0:
                ans.append(v[:k])
                v = v[k:]
        return ans

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math
        def check(n):
            return sum(list(map(lambda x: math.ceil(x / n), nums)))

        start = 1
        end = max(nums)

        while True:
            if start == end:
                return start
            mid = (start + end) // 2
            if check(mid) > threshold:
                start = mid + 1
            else:
                end = mid

    def encoder(self, mat):
        l = []
        for line in mat:
            l += line

        return int(''.join(l), base=2)

    def decoder(self, num, m, n):
        l = list(bin(num)[2:])
        mat = []
        for i in range(m):
            mat.append(l[i * n:(i + 1) * n])
        return mat

    def minFlips(self, mat: List[List[int]]) -> int:
        import queue
        import copy

        m = len(mat)
        n = len(mat[0])
        q = queue.Queue()
        d = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
        # start_state = self.encoder(mat)
        # start_state = mat
        step = 0
        if sum(list(map(sum, mat))) == 0:
            return step
        # visited = {start_state}
        q.put_nowait(mat)
        while step < m * n:
            step += 1
            k = q.qsize()
            for aa in range(k):
                state = copy.deepcopy(q.get_nowait())
                q.put_nowait(copy.deepcopy(state))  # 对应位不翻
                # mmat = self.decoder(state,m,n)  # 对应位翻
                i = (step - 1) // n
                j = (step - 1) % n
                for dd in d:
                    ii = i + dd[0]
                    jj = j + dd[1]
                    if 0 <= ii < m and 0 <= jj < n:
                        state[ii][jj] = int(not state[ii][jj])
                if sum(list(map(sum, state))) == 0:
                    return sum(list(map(int, bin(aa)[2:]))) + 1
                else:
                    q.put_nowait(state)
        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
    # print(s.smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11))
    # print(s.smallestDivisor(nums=[19], threshold=5))
    print(s.minFlips([[0,0],[0,1]]))
    print(s.minFlips([[0]]))
    print(s.minFlips([[1,1,1],[1,0,1],[0,0,0]]))
    print(s.minFlips([[1,0,0],[1,0,0]]))
    print(s.minFlips([[1],[0]]))