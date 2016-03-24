'''
排序后，头尾指针逼近
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        m = list(enumerate(num))
        m.sort(key=lambda a:a[1])
        index1, index2 = 0, len(num)-1
        while index1 != index2:
            sum = m[index1][1] + m[index2][1]
            if sum > target:
                index2 -= 1
            elif sum < target:
                index1 += 1
            else:
                ret = (m[index1][0]+1, m[index2][0]+1)
                if ret[0] > ret[1]:
                    ret = (ret[1], ret[0])
                return ret



if __name__ == '__main__':
    print Solution().twoSum([-2,3,3], 6)