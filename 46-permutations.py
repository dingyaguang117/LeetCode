'''
# solution 1

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 1:
            return [num]
        if len(num) == 2:
            return [[num[0], num[1]], [num[1], num[0]]]  
        ret = []
        for i in xrange(len(num)):
            _ret = self.permute(num[:i] + num[i+1:])
            ret.extend([[num[i]] + one for one in _ret])
        return ret
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def _permute(self, num, begin):
        if begin == self.length - 1:
            self.ret.append(num[:])
        for i in xrange(begin, self.length):
            num[begin], num[i] = num[i], num[begin]
            self._permute(num, begin+1)
            num[begin], num[i] = num[i], num[begin]

    def permute(self, num):
        self.length = len(num)
        self.ret = []
        self._permute(num, 0)
        return self.ret




if __name__ == '__main__':
    print Solution().permute([1,2,3])