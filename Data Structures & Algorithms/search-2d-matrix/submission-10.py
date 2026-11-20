class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = t+(b-t)//2

            if matrix[mid][0]<=target<=matrix[mid][-1]:
                break
            elif matrix[mid][0]>target:
                b = mid - 1
            elif matrix[mid][-1]<target:
                t = mid +1

        l, r = 0, len(matrix[0]) -1
        while l<=r:
            m = l+(r-l)//2

            if target == matrix[mid][m]:
                return True
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                r = m - 1
        return False




















        