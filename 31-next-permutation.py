class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # find first position from right which num[pos] < num[pos+1]
        pos = None
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pos = i
                break

        if pos is None:
            nums.reverse()
            return

        # find the minimum number after pos, swap them, then reverse the slice after pos
        best = None
        for i in xrange(pos+1, len(nums)):
            if best is None:
                best = i
            elif nums[i] > nums[pos] and nums[i] <= nums[best]:
                best = i

        nums[pos], nums[best] = nums[best], nums[pos]
        nums[pos+1:] = nums[pos+1:][::-1] 


if __name__ == '__main__':
    s = Solution()
    s.nextPermutation([2,3,1,3,3])