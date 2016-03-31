class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in xrange(2, n+1):
        	for j in xrange(0, i):
        		dp[i] += dp[j]*dp[i-j-1]
        return dp[n]

if __name__ == '__main__':
	s = Solution()
	assert s.numTrees(1) == 1
	assert s.numTrees(2) == 2
	assert s.numTrees(3) == 5