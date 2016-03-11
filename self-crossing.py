#coding=utf-8
class Solution(object):

    def cross_product(self, v1, v2):
        return v1[0]*v2[1] - v1[1]*v2[0]

    def angel(self, v1, v2, v3):
        return self.cross_product(v1, v2) * self.cross_product(v1, v3)

    def isSimpleCrossing(self, line1, line2):
        a1, a2  = line1
        b1, b2 = line2
        
        ax_min, ax_max, = min(a1[0], a2[0]), max(a1[0], a2[0])
        ay_min, ay_max, = min(a1[1], a2[1]), max(a1[1], a2[1])
        bx_min, bx_max, = min(b1[0], b2[0]), max(b1[0], b2[0])
        by_min, by_max, = min(b1[1], b2[1]), max(b1[1], b2[1])

        if ax_max < bx_min or ay_max < by_min or bx_max < ax_min or by_max < ay_min:
            return False
        return True

    def isCrossing(self, line1, line2):
        a1, a2 = line1
        b1, b2 = line2

        v1 = (a2[0]-a1[0], a2[1]-a1[1])
        v2 = (b1[0]-a1[0], b1[1]-a1[1])
        v3 = (b2[0]-a1[0], b2[1]-a1[1])

        v4 = (b2[0]-b1[0], b2[1]-b1[1])
        v5 = (a1[0]-b1[0], a1[1]-b1[1])
        v6 = (a2[0]-b1[0], a2[1]-b1[1])

        angel1 = self.angel(v1, v2, v3)
        angel2 = self.angel(v4, v5, v6)
        #on a line
        if angel1 <=0 and angel2 <=0:
            return True
        else:
            return False


    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        paths = []
        directs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        direct = 0
        pos = (0, 0)

        for step in x:
            deta = directs[direct]
            #latest step:
            line = (pos, (pos[0]+step*deta[0], pos[1]+step*deta[1]))
            print 'step:', line
            
            for path in paths[-5:-1]:
                if self.isSimpleCrossing(line, path) and self.isCrossing(line, path):
                    print 'cross:', line, path
                    return True
            
            direct += 1
            direct %= 4
            pos = line[1]
            paths.append(line)
        return False


if __name__ == '__main__':
    s = Solution()

    x = [1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1]
    assert s.isSelfCrossing(x) == False
    x = [1,1,2,1,1]
    assert s.isSelfCrossing(x) == True
    x = [1, 2, 3, 4]
    assert s.isSelfCrossing(x) == False
    x = [2,1,4,4,3,3,2,1,1]
    assert s.isSelfCrossing(x) == True