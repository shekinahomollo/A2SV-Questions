class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        lines = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lines[i+j].append(mat[i][j])
        for k in range(len(mat) + len(mat[0]) - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res