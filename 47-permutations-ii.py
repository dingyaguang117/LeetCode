class Solution:
    def _permute(self, num, begin):
        if begin == self.length - 1:
            self.ret.append(num[:])
        for i in xrange(begin, self.length):
            flag = False
            for j in xrange(begin, i):
                if num[j] == num[i]:
                    flag = True
                    break
            if flag:
                continue
            num[begin], num[i] = num[i], num[begin]
            self._permute(num, begin+1)
            num[begin], num[i] = num[i], num[begin]

    def permuteUnique(self, num):
        self.length = len(num)
        self.ret = []
        num.sort()
        self._permute(num, 0)
        return self.ret



if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 1, 2])