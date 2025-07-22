from colors import Colors

class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.size=30
        self.row_offset = 0
        self.col_offset = 0
        self.state=0
        self.colors = Colors.get_colors()

    def move(self,rows,cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_positions(self):
        tiles = self.cells[self.state]
        return [Position(position.row + self.row_offset,
                         position.col + self.col_offset)
                for position in tiles]

    def rotate(self):
        if self.state >= len(self.cells)-1:
            self.state = 0
        else: self.state += 1  
    
    def unrotate(self):
        if self.state == 0:
            self.state = len(self.cells)-1
        else: self.state -=1

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1,0),Position(1,1),Position(1,2),Position(0,2)],
            1: [Position(2,1),Position(2,2),Position(1,1),Position(0,1)],
            2: [Position(2,0),Position(1,0),Position(1,1),Position(1,2)],
            3: [Position(2,1),Position(1,1),Position(0,0),Position(0,1)]
        }
        self.spawn_row = 0
        self.spawn_col = 3
        self.move(self.spawn_row,self.spawn_col)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 0)],
            1: [Position(2, 1), Position(1, 1), Position(0, 1), Position(0, 2)],
            2: [Position(2, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            3: [Position(2, 0), Position(2, 1), Position(1, 1), Position(0, 1)]
        }
        self.spawn_row = 0
        self.spawn_col = 3
        self.move(self.spawn_row,self.spawn_col)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(3, 2), Position(2, 2), Position(1, 2), Position(0, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(3, 1), Position(2, 1), Position(1, 1), Position(0, 1)]
        }
        self.spawn_row = 0
        self.spawn_col = 3
        self.move(self.spawn_row,self.spawn_col)

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(0, 0), Position(0, 1) ]
        }
        self.spawn_row = 0
        self.spawn_col = 4
        self.move(self.spawn_row,self.spawn_col)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(0, 1), Position(0, 2)],
            1: [Position(2, 2), Position(1, 1), Position(1, 2), Position(0, 1)],
            2: [Position(2, 0), Position(2, 1), Position(1, 1), Position(1, 2)],
            3: [Position(2, 1), Position(1, 0), Position(1, 1), Position(0, 0)]
        }
        self.spawn_row = 0
        self.spawn_col = 3
        self.move(self.spawn_row,self.spawn_col)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 1)],
            1: [Position(2, 1), Position(1, 1), Position(1, 2), Position(0, 1)],
            2: [Position(2, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            3: [Position(2, 1), Position(1, 0), Position(1, 1), Position(0, 1)]
        }
        self.spawn_row = 0
        self.spawn_col = 3
        self.move(self.spawn_row,self.spawn_col)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(1, 1), Position(1, 2), Position(0, 0), Position(0, 1)],
            1: [Position(2, 1), Position(1, 1), Position(1, 2), Position(0, 2)],
            2: [Position(2, 1), Position(2, 2), Position(1, 0), Position(1, 1)],
            3: [Position(2, 0), Position(1, 0), Position(1, 1), Position(0, 1)]
        }
        self.spawn_row = 0
        self.spawn_col = 3
        self.move(self.spawn_row,self.spawn_col)

class Position:
    def __init__(self,row,col):
        self.row = row
        self.col = col