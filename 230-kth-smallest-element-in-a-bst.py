# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _find(self, root, k, total):
        if root is None:
            return None, total
        result, total = self._find(root.left, k, total)

        if result:
            return result, total

        total += 1
        if total == k:
            return root, total

        result, total = self._find(root.right, k, total)
        return result, total

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        return self._find(root, k, 0)[0].val