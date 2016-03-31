'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sum1, sum2 = 0, 0
        for i in xrange(1, length):
        	sum1 ^= i
        for i in nums:
        	sum2 ^= i
        return sum1 ^ sum2
'''

class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        prev = None
        for num in nums:
        	if num == prev:
        		return prev
        	prev = num


if __name__ == '__main__':
	s = Solution()
	print s.findDuplicate([1,2,3,4,5,6, 4])
