from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.size = 30
        self.grid = [[0]*self.cols for _ in range(self.rows)]
        self.colors = Colors.get_colors()

    def printGrid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = " ")
            print()

    def out_of_bounds(self,row,col):
        return not (row >= 0 and row < self.rows and col >= 0 and col < self.cols)
    
    def is_occupied(self,row,col):
        return not (self.grid[row][col] == 0)
    
    def is_full(self,row):
        for col in range(self.cols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clear_row(self,row):
        for col in range(self.cols):
            self.grid[row][col] = 0

    def collapse(self,row,num):
        for col in range(self.cols):
            self.grid[row+num][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def check_rows(self):
        lines = 0
        for row in range(self.rows-1,0,-1):
            if self.is_full(row):
                self.clear_row(row)
                lines +=1
            elif lines >0:
                self.collapse(row,lines)
        return lines