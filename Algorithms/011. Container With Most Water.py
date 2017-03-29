class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        top_hight = 0
        max_contain = 0
        hight_position = {}
        width = len(height)
        ans = 0
        if len(height) >= 2:
            for i in range(len(height)):
                temp_value = height[i]
                top_hight = max(top_hight, temp_value)
                if temp_value not in hight_position:
                    hight_position[temp_value] = {
                        "M" : i,
                        "m" : i
                        }
                else:
                    hight_position[temp_value]["M"] = max(hight_position[temp_value]["M"], i)
                    hight_position[temp_value]["m"] = min(hight_position[temp_value]["m"], i)
            
            boundary = {
                "M" : hight_position[top_hight]["M"],
                "m" : hight_position[top_hight]["m"]
                }
            
            for h in range(top_hight, -1, -1):
                if ans >= h * width:
                    break
                elif h in hight_position:
                    boundary["M"] = max(hight_position[h]["M"], boundary["M"])
                    boundary["m"] = min(hight_position[h]["m"], boundary["m"])
                    ans = max(ans, h * (boundary["M"] - boundary["m"]) )
                
        return ans