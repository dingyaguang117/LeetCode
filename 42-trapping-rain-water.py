class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if not length:
            return 0

        lmax = [0] * length
        rmax = [0] * length
        ans = 0

        lmax[0] = height[0]
        for i in xrange(1, length):
            lmax[i] = max(height[i], lmax[i-1])

        rmax[length-1] = height[length-1]
        for i in xrange(length-2, -1, -1):
            rmax[i] = max(height[i], rmax[i+1])

        for i in xrange(1, length-1):
            ans += max(min(lmax[i-1], rmax[i+1]) - height[i], 0)

        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([0]) == 0
    assert s.trap([0,1]) == 0
    assert s.trap([]) == 0
    assert s.trap([1, 2, 3]) == 0
    assert s.trap([1, 2, 1]) == 0
    assert s.trap([1, 0, 1]) == 1