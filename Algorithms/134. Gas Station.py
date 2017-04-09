class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        gas_change = []
        sorted_gc = [[0,0]]
        s = len(gas)
        for i in range(s):
            g_change = gas[i] - cost[i]
            if g_change * sorted_gc[-1][0] < 0:
                sorted_gc.append([g_change, i])
            else:
                sorted_gc[-1][0] += g_change
        
        ss = len(sorted_gc)
        print(sorted_gc)
        for i in range(ss):
            if sorted_gc[i][0] >= 0:
                gas_remain = 0
                for j in range(ss):
                    gas_remain += sorted_gc[(i+j) % ss][0]
                    if gas_remain < 0:
                        break
                    
                    if j == ss - 1:
                        return sorted_gc[i][1]
        
        return -1