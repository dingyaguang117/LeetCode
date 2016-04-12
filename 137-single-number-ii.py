class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        for num in nums:
            mask = 1
            for i in xrange(32):
                bits[i] += 1 if num & mask > 0 else 0
                mask <<= 1

        ret = 0
        base = 1
        sign = 1

        if bits[-1] %3 == 1:
            sign = -1

        for i in xrange(32):
            if bits[i] % 3:
                ret += base
            base <<= 1

        if sign == -1:
            ret = 0xffffffff ^ ret 
            ret += 1
            ret = -ret

        return ret



if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([-1,-1,-1,2,2,2, -3])