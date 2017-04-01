# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            ans = [newInterval]
        else:
            rank = [0,0]
            if newInterval.start > intervals[-1].end:
                rank[0] = 2 * len(intervals)
            else:
                for i in range(2 * len(intervals)):
                    if i % 2 ==0:
                        if newInterval.start < intervals[int(i / 2)].start:
                            rank[0] = i
                            break
                    else:
                        if newInterval.start <= intervals[int(i / 2)].end:
                            rank[0] = i
                            break
            
            if newInterval.end > intervals[-1].end:
                rank[1] = 2 * len(intervals)
            else:
                for i in range(2 * len(intervals)):
                    if i % 2 ==0:
                        if newInterval.end < intervals[int(i / 2)].start:
                            rank[1] = i
                            break
                    else:
                        if newInterval.end <= intervals[int(i / 2)].end:
                            rank[1] = i
                            break
            
            insert_inter = Interval(0,0)
            
            if rank[0] % 2 == 0:
                insert_inter.start = newInterval.start
            else:
                insert_inter.start = intervals[int(rank[0] / 2)].start
            
            if rank[1] % 2 == 0:
                insert_inter.end = newInterval.end
            else:
                insert_inter.end = intervals[int(rank[1] / 2)].end
            
            ans = intervals[:int(rank[0] / 2)] + [insert_inter] + intervals[int((rank[1] + 1) / 2):]
            
            print(rank)
        
        return ans
            