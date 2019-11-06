# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def _find(self, root, p, q):

        if root is None:
            return None, 0

        result1, count1 = self._find(root.left, p, q)
        if result1:
            return result1, 2

        result2, count2 = self._find(root.right, p, q)
        if result2:
            return result2, 2


        count = count1 + count2 + (1 if root is p or root is q else 0)
        if count == 2:
            return root, 2
        return None, count



    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        return self._find(root, p, q)[0]



solution = Solution()

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
a.right = c

print solution.lowestCommonAncestor(a, b, c)

