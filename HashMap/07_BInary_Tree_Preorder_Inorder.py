"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, construct
and return the binary tree.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        index = {}

        for i in range(len(inorder)):
            index[inorder[i]] = i

        self.pre = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre]
            self.pre += 1

            root = TreeNode(root_val)

            mid = index[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
    
    def display(self, root, level=0):
        if root is not None:
            Solution().display(root.right, level + 1)
            print("    " * level + str(root.val))
            Solution().display(root.left, level + 1)

root = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
Solution().display(root)

# print(Solution().buildTree([3,9,20,15,7],[9,3,15,20,7]))