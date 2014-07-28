class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return self._permute(num)


    def _permute(self, num):
        if len(num) == 1:
            return [num]
        if len(num) == 2:
            return [[num[0], num[1]], [num[1], num[0]]]  
        ret = []
        for i in xrange(len(num)):
            _ret = self._permute(num[:i] + num[i+1:])
            ret.extend([[num[i]] + one for one in _ret])
        return ret


if __name__ == '__main__':
    print Solution().permute([1,2,3])