class Solution:
    def countAndSay(self, n: int) -> str:
        for t in range(n):
            if t==0:
                output="1"
            else:
                new_output = ""
                temp_char = output[0]
                count = 1
                for s in output[1:]:
                    if temp_char==s:
                        count += 1
                    else:
                        new_output += "{}{}".format(count, temp_char)
                        temp_char = s
                        count = 1
                
                new_output += "{}{}".format(count, temp_char)
                output = ""+new_output
        
        return output