class Solution(object):
    max_length = 0
    def deep_search(self, x, y):
        if self.value_matrix[x][y]:
            return self.value_matrix[x][y]
        else:
            self.value_matrix[x][y] = 1
        for i,j in [(-1,0),(0,1),(1,0),(0,-1)]:
            new_x = x + i
            new_y = y + j
            if new_x>=0 and new_x<self.x_len and new_y>=0 and new_y<self.y_len and \
                self.matrix[new_x][new_y]>self.matrix[x][y]:
                self.value_matrix[x][y] = max(self.value_matrix[x][y], self.deep_search(new_x, new_y)+1)
        if self.value_matrix[x][y] > self.max_length:
            self.max_length = self.value_matrix[x][y]
        return self.value_matrix[x][y]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        self.x_len = len(self.matrix)
        if self.x_len == 0:
            return 0
        self.y_len = len(self.matrix[0])
        self.value_matrix = [[0 for m in range(self.y_len)] for n in range(self.x_len)]
        for i in range(self.x_len):
            for j in range(self.y_len):
                self.deep_search(i, j)
        return self.max_length
