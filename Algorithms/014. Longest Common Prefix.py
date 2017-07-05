class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp_bool = True
        if len(strs) > 0:
            shortest = len(strs[0])
            for s in strs:
                shortest = min(shortest, len(s))
            out_put = ""
            i = 0
            while temp_bool:
                if i == shortest:
                    break
                car = strs[0][i]
                for s in strs:
                    if s[i] != car:
                        temp_bool = False
                        break

                if temp_bool:
                    out_put += car
                    i += 1

            return out_put
        
        else:
            return ""
        