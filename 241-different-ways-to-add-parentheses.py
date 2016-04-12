class Solution(object):

    def compute(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b

    def calc(self, start, end):
        if (start, end) in self.mem:
            return self.mem[(start, end)]
        if start == end:
            return [self.nums[start]]
        if start+1 == end:
            return [self.compute(self.nums[start], self.nums[end], self.operations[start])]
        ans = []
        for mid in xrange(start, end):
            left = self.calc(start, mid)
            right = self.calc(mid+1, end)
            for item in left:
                for item2 in right:
                    ans.append(self.compute(item, item2, self.operations[mid]))

        self.mem[(start, end)] = ans      
        return ans


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.mem = {}
        self.nums = []
        self.operations = []

        num = ''
        for char in input:
            if char in ['-', '+', '*']:
                self.nums.append(int(num))
                num = ''
                self.operations.append(char)
                continue
            num += char
        self.nums.append(int(num))
        ans = self.calc(0, len(self.nums)-1)
        ans.sort()
        return ans



if __name__ == '__main__':
    s = Solution()
    print s.diffWaysToCompute("2-1-1")
    print s.diffWaysToCompute("2*3-4*5")