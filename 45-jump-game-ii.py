from collections import deque

'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length

        for i in xrange(length):
        	for step in xrange(1, nums[i]+1):
        		if i+step >= length:
        			break
        		dp[i+step] = dp[i]+1 if dp[i+step] == 0 else min(dp[i+step], dp[i]+1)
        return dp[length-1]
'''

class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		length = len(nums)
		dp = [None] * length
		queue = deque([])
		queue.append(0)
		dp[0] = 0

		while queue:
			item = queue.popleft()
			for i in xrange(item+1, item+nums[item]+1):
				if i >= length:
					continue
				if not dp[i]:
					dp[i] = dp[item]+1
					if i == length-1:
						return dp[i]
					queue.append(i)
		return dp[length-1]


if __name__ == '__main__':
	s = Solution()
	print range(1,25001)[::-1] + [1, 0]
	print s.jump(range(1,25001)[::-1] + [1, 0])
	print s.jump([2,3,1,1,4])
	print s.jump([2,1])
