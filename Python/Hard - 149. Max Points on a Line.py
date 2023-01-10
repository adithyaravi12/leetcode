#	https://leetcode.com/problems/max-points-on-a-line/description/

#	test cases: passed
#	submission: failed

class Solution:
    def maxPoints(self, points):
        """
         :type points: List[List[int]]
         :rtype: int
        """
        count_val = 1
        if len(points) == 1:
            return count_val
        # print("point len = ",len(points))
        for i in range(0,len(points)):
            # print("i = ", i)
            slope_count = {}
            for j in range(i+1,len(points)):
                # print("j = ",j)
                perp_slop_check = points[j][0] - points[i][0]
                if perp_slop_check == 0: 
                    m = 'INF'
                else:
                    # print("[i][0] = ", points[i][0])
                    # print("[i][1] = ",points[j][1])
                    # print("[j][0] = ", points[i][0])
                    # print("[j][1] = ",points[j][1])
                    m = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) 
                    # print("m =", m)
                if m in slope_count: 
                    slope_count[m] += 1
                    # print("slope_count =", slope_count[m])
                else:
                    slope_count[m] = 1
                    # print("slope_count value set: ", slope_count[m])
            for i in slope_count: 
                count_val = max(count_val ,slope_count[i]+1)
                # print("count_val =", count_val)
        return count_val

                
