class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        matrix = []
        a = 0
        b = n
        if len(original) != (m*n):
            return matrix
        else:
            for i in range(0,m):
                row = []
                for i in range(a,b):
                    row.append(original[i])
                matrix.append(row)
                a += n
                b += n

            return matrix