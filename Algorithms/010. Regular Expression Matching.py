def extract_pattern(p: str) -> (str, str, bool):
    """
    extract next pattern p[0], and cheak p[1]==*
    return :
    remain pattern
    symbol : next pattern = p[0]
    unlimit_match : (p[1]==*)
    """
    symbol = p[0]
    unlimit_match = False
    if len(p) >= 2:
        if p[1] == '*':
            unlimit_match = True
            return p[2:], symbol, unlimit_match
    
    return p[1:], symbol, unlimit_match

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp_table = [[True]+[False]*(len(s))] # table for dynamic programming        
        while p != '':
            p, symbol, unlimit_match = extract_pattern(p)
            next_table = [False]*(len(s)+1)
            for i in range(len(s)+1):
                if dp_table[-1][i]:
                    if unlimit_match:
                        next_table[i]=True
                    
                    if (i < len(s)):
                        if symbol in [s[i], '.']:
                            next_table[i+1] =True
                            if unlimit_match:
                                dp_table[-1][i+1] = True
                
            dp_table.append(next_table)
        
        return dp_table[-1][-1]