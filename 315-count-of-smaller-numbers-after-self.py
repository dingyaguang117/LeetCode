class BST(object):
    
    def __init__(self, size):
        self.size = size
        self.x = [0] * (size + 1)

    def lowbit(self, n):
        return ((n-1)^n)&n

    def add(self, pos, num):
        while pos <= self.size:
            self.x[pos] += num
            pos += self.lowbit(pos)

    def sum(self, pos):
        ans = 0
        while pos > 0:
            ans += self.x[pos]
            pos -= self.lowbit(pos)
        return ans


class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        size = max(nums) - min(nums) + 1
        offset = 1 - min(nums)

        print size, offset

        bst = BST(size)
        ret = [0] * len(nums)

        for i in xrange(len(nums)-1, -1, -1):
            num = nums[i] + offset
            ret[i] = bst.sum(num-1)
            bst.add(num, 1)
        return ret

if __name__ == '__main__':
    s = Solution()
    assert s.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert s.countSmaller([-1]) == [0]