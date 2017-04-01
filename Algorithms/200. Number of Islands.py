class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        hig = len(grid)
        wid = len(grid[0])
        diffusion_list = []
        ex_grid = [["0"] * (wid + 2)]
        for i in range(hig):
            ex_grid.append(["0"] + grid[i] + ["0"])
        ex_grid.append(["0"] * (wid + 2))
        
        ans = 0
        for i in range(1, hig + 1):
            for j in range(1, wid + 1):
                if ex_grid[i][j] == "1":
                    diffusion_list.append([i,j])
                    ex_grid[i][j] = "0"
                    while diffusion_list != []:
                        center = diffusion_list[0]
                        diffusion_list = diffusion_list[1:]
                        for h, v in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            tar_p = [center[0] + h, center[1] + v]
                            if ex_grid[tar_p[0]][tar_p[1]] == "1":
                                diffusion_list.append(tar_p)
                                ex_grid[tar_p[0]][tar_p[1]] = "0"
                    
                    
                    ans += 1
        
        return ans