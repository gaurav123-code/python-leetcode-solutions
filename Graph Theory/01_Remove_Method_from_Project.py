"""
You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where
invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly
or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return 
the answer in any order. If it is not possible to remove all the suspicious methods, none
should be removed.
"""

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    stack.append(nei)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
    

print(Solution().remainingMethods(4,1,[[1,2],[0,1],[3,2]]))
