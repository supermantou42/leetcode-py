from typing import *


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1 = len(str1)
        len_2 = len(str2)
        max_len = min(len_1, len_2)
        for i in range(min(len_1, len_2)):
            if str1[i] != str2[i]:
                max_len = i
                break
        gcd_pattern = ''
        for i in range(1, max_len + 1)[::-1]:
            if len_1 % i == 0 and len_2 % i == 0:
                pattern = str1[:i]
                if str1.count(pattern) == len_1 // i and str2.count(pattern) == len_2 // i:
                    return pattern
        return gcd_pattern

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        line_weight = {}
        for line in matrix:
            key = tuple(line) if line[0] == 0 else tuple([1-i for i in line])
            if not line_weight.__contains__(key):
                line_weight[key] = 1
            else:
                line_weight[key] += 1
        return max(line_weight.values())
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_len = max(len(arr1), len(arr2)) + 2
        arr1 = [0] * (max_len - len(arr1)) + arr1
        arr2 = [0] * (max_len - len(arr2)) + arr2
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        flag = 0
        ans = [0] * max_len
        for i in range(max_len):
            s = arr1[i] + arr2[i] + flag
            if s == 2:
                flag = -1
                ans[i] = 0
            elif s == 3:
                flag = -1
                ans[i] = 1
            elif s == -1:
                flag = -1 if flag != -1 else 1
                ans[i] = 1
            else:
                flag = 0
                ans[i] = s
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop(-1)
        return ans[::-1]

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        len_row = len(matrix)
        len_col = len(matrix[0])
        d = [[0] * len_col for _ in range(len_row)]
        matrix_sum = matrix.copy()
        for i in range(1,len_col):
            matrix_sum[0][i] += matrix_sum[0][i-1]
        for j in range(1,len_row):
            matrix_sum[i][0] += matrix_sum[i-1][0]
        for i in range(1,len_row):
            for j in range(1,len_col):
                matrix_sum[i][j] += matrix_sum[i-1][j] + matrix_sum[i][j-1] - matrix_sum[i-1][j-1]

        d[0][0] = 1 if matrix[0][0] == target else 0
        for i in range(1, len_col):
            cnt = 0
            total = 0
            for j in range(i+1)[::-1]:
                total += matrix[0][j]
                if total == target:
                    cnt += 1
            d[0][i] = d[0][i-1] + cnt

        for i in range(1, len_row):
            cnt = 0
            total = 0
            for j in range(i+1)[::-1]:
                total += matrix[j][0]
                if total == target:
                    cnt += 1
            d[i][0] = d[i-1][0] + cnt

        for i in range(1,len_row):
            for j in range(1,len_col):
                cnt = 0
                for ii in range(1,i+2): # 行数1~i+1
                    total = 0
                    for jj in range(j+1)[::-1]: # 列号j~0
                        for iii in range(ii):
                            total += matrix[i-iii][jj]
                        if total == target:
                            cnt += 1
                d[i][j] = d[i-1][j] + d[i][j-1] + cnt - d[i-1][j-1]

        return d[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numSubmatrixSumTarget(matrix = [[0,0,0,1,1],[1,1,1,1,1],[0,1,0,0,0],[0,1,0,0,0],[1,1,1,1,0],[1,1,1,0,1]], target = 0))
    # print(s.addNegabinary(arr1=[1], arr2=[1]))
    # print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
