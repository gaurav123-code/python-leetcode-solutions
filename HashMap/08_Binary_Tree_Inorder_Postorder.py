"""
Given two integer arrays inorder and postorder where inorder is the inorder 
traversal of a binary tree and postorder is the postorder traversal of the same tree, 
construct and return the binary tree.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        index = {}

        for i in range(len(inorder)):
            index[inorder[i]] = i

        self.post = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            root_val = postorder[self.post]
            self.post -= 1

            root = TreeNode(root_val)

            mid = index[root_val]

            # Right subtree pehle
            root.right = build(mid + 1, right)

            # Left subtree baad me
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)

print(Solution().buildTree([9,3,15,20,7],[9,15,7,20,3]))