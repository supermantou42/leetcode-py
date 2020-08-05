from typing import *
import time


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = [(c + 1) // 2 for c in coins]
        return sum(ans)

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        rm = [[] for _ in range(n)]
        for r in relation:
            rm[r[0]].append(r[1])
        prev = [0]
        next_ = []
        for i in range(k):
            next_ = []
            for ni in prev:
                next_.extend(rm[ni])
            prev = next_
        return next_.count(n - 1)

    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        n_req = len(requirements)
        n_days = len(increase)
        ans = [[-1] * 3 for _ in range(n_req)]
        for t in range(3):
            inc = [inc_[t] for inc_ in increase]
            r = [(re[t], idx) for idx, re in enumerate(requirements)]
            r.sort(key=lambda x: x[0])
            value = 0
            ridx = 0
            while ridx < n_req and r[ridx][0] <= value:
                ans[r[ridx][1]][t] = 0
                ridx += 1
            for day in range(1, n_days + 1):
                value += inc[day - 1]
                while ridx < n_req and r[ridx][0] <= value:
                    ans[r[ridx][1]][t] = day
                    ridx += 1
                if ridx == n_req:
                    break
        return [max(a) if min(a) > -1 else -1 for a in ans]

    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        visited = [False]*n
        min_l = [n]
        def dfs(idx,depth):
            if depth >= min_l[0]:
                return
            visited[idx] = True

            if idx+jump[idx] >= n:
                min_l[0] = min(depth,min_l[0])
                return
            else:
                dfs(idx+jump[idx],depth+1)

            for i in range(idx):
                if not visited[i]:
                    dfs(i,depth+1)

            visited[idx] = False
        dfs(0,0)
        return min_l[0]
        # n = len(jump)
        # i = 0
        # t = 0
        # j = [-1]*n
        # lastmax = -1
        # maxj = jump[0]
        # while maxj < n:
        #     for ii in range(lastmax+1,maxj+1):
        #         j[ii] = ii + jump[ii]
        #     _tmp = max(j[lastmax+1:maxj+1])
        #     if _tmp >= n:
        #         return t
        #     if _tmp == maxj + jump[maxj]:
        #         t+=1
        #     else:
        #         t+=2
        #     # if _tmp <= maxj:
        #     #     return -1
        #
        # # mj = [-1]*n
        # # mj[0] = 0
        # # prev = [0]
        # # next_ = []
        # # i = 1
        # # while len(prev) > 0:
        # #     for p in prev:
        # #         if p + jump[p] < n and mj[p + jump[p]] == -1:
        # #             mj[p + jump[p]] = i
        # #             next_.append(p + jump[p])
        # #     prev = next_
        # #



    def minimalExecTime(self, root: TreeNode) -> float:
        parent = []
        job_time = []
        sub_n = []
        leaf_node = []
        node_cnt = [0]

        def dfs(node: TreeNode,pid):
            if node is None:
                return 0
            nid = node_cnt[0]
            job_time.append(node.val)
            sub_n.append(0)
            parent.append(pid)
            node_cnt[0]+=1
            if node.left is None and node.right is None:
                leaf_node.append(nid)
            sub_n[nid] += dfs(node.left,nid)
            sub_n[nid] += dfs(node.right,nid)
            return 1

        dfs(root,-1)
        ans = 0
        while len(leaf_node) > 0:
            if len(leaf_node) == 1:
                ans+=job_time[leaf_node[0]]
                pid = parent[leaf_node[0]]
                if pid == -1:
                    break
                sub_n[pid]-=1
                if sub_n[pid] == 0:
                    leaf_node = [pid]
            else:
                leaf_node.sort(key=lambda x:job_time[x],reverse=True)
                ans += job_time[leaf_node[1]]
                job_time[leaf_node[0]] -= job_time[leaf_node[1]]
                pid = parent[leaf_node[1]]
                if pid == -1:
                    break
                sub_n[pid]-=1
                if sub_n[pid] == 0:
                    leaf_node.append(pid)
                leaf_node.pop(1)

                if job_time[leaf_node[0]] == 0:
                    pid = parent[leaf_node[0]]
                    if pid == -1:
                        break
                    sub_n[pid] -= 1
                    if sub_n[pid] == 0:
                        leaf_node.append(pid)
                    leaf_node.pop(0)
        return ans





if __name__ == '__main__':
    s = Solution()
    print(s.minJump(jump = [2, 5, 1, 1, 1, 1]))
    # print(s.getTriggerTime(increase=[[2, 8, 4], [2, 5, 0], [10, 9, 8]],
    #                        requirements=[[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]))
    # print(s.getTriggerTime(increase=[[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]],
    #                        requirements=[[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]]))
    # print(s.getTriggerTime(increase=[[1, 1, 1]], requirements=[[0, 0, 0]]))
