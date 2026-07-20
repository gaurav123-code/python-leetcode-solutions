    m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        if k == 0:
            return grid
            
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                current_1d_index = i * n + j
                new_1d_index = (current_1d_index + k) % total_elements
                
                new_row = new_1d_index // n
                new_col = new_1d_index % n
                
                result[new_row][new_col] = grid[i][j]
                
        return result