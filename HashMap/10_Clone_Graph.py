"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []
        
class Solution(object):
    def cloneGraph(self, node):

        if not node:
            return None

        cloned = {}

        def dfs(curr):

            if curr in cloned:
                return cloned[curr]

            copy = Node(curr.val)
            cloned[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

# print(Solution().cloneGraph([[2,4],[1,3],[2,4],[1,3]]))

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

clone = Solution().cloneGraph(n1)
print(clone.val)