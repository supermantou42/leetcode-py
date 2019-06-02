from typing import *


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_x, pos_y = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        now_direction = 0
        for _ in range(4):
            for char in instructions:
                if char == 'G':
                    pos_x += direction[now_direction][0]
                    pos_y += direction[now_direction][1]
                elif char == 'L':
                    now_direction = (now_direction - 1) % 4
                else:
                    now_direction = (now_direction + 1) % 4
            if pos_x == 0 and pos_y == 0:
                return True
        return False

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        answer = [0] * N
        road_map = {}
        for i in range(N):
            road_map[i + 1] = []
        for path in paths:
            road_map[path[0]].append(path[1])
            road_map[path[1]].append(path[0])

        def isok(pos: int, color: int) -> bool:
            neibor = road_map[pos]
            for n in neibor:
                if answer[n - 1] == color:
                    return False
            return True

        def go(pos: int) -> bool:
            if pos > N:
                return True
            for c in range(4):
                if isok(pos, c + 1):
                    answer[pos - 1] = c + 1
                    if go(pos + 1):
                        return True
                    answer[pos - 1] = 0

        go(1)
        return answer

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        d = [0] * len(A)
        for i in range(K):
            d[i] = max(A[0:i + 1]) * (i + 1)
        for i in range(len(A))[K:]:
            for j in range(K):
                value = d[i - j - 1] + max(A[i-j:i+1]) * (j + 1)
                if value > d[i]:
                    d[i] = value
        return d[-1]

    def maxSumAfterPartitioning_no(self, A: List[int], K: int) -> int:
        length = len(A)

        def go(start, now_sum, max_sum):
            left = length - start
            for i in range(min(left, K)):
                max_value = max(A[start:start + i + 1])
                now_sum += max_value * (i + 1)
                max_sum = go(start + i + 1, now_sum, max_sum)
                now_sum -= max_value * (i + 1)
            if left < K:
                if now_sum > max_sum:
                    max_sum = now_sum
                return max_sum
            return max_sum

        return go(0, 0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
