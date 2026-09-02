class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        row_min = []
        col_max = []
        
        # Find minimum of every row
        for row in matrix:
            row_min.append(min(row))
        
        # Find maximum of every column
        for j in range(len(matrix[0])):
            maximum = matrix[0][j]
            
            for i in range(len(matrix)):
                maximum = max(maximum, matrix[i][j])
            
            col_max.append(maximum)
        
        # Common elements are lucky numbers
        result = []
        
        for num in row_min:
            if num in col_max:
                result.append(num)
        
        return result