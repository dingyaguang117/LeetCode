# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        stack = []
        p = root
        left_visited = False

        while True:
            if not left_visited:
                while p.left:
                    stack.append(p)
                    p = p.left
            
            ans.append(p.val)
            if p.right:
                p = p.right
                left_visited = False
                continue
            
            if stack:
                p = stack.pop()
                left_visited = True
                continue
            break
        return ans