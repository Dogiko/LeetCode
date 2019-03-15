class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        
        output = 1
        while 4*output*output<=x:
            output *= 2
        
        step = output/2
        while step>=1:
            if x >= (output+step)*(output+step):
                output += step
            
            step /= 2
        
        return int(output)