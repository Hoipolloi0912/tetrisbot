from grid import Grid
from blocks import *
import random,pygame,copy

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.count = 0
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.score_value = [5,100,300,800,2000]
        self.tetris_count = 0 #count tetris, evolution algorithm

    def get_random_block(self):
        self.count +=1
        if not self.blocks: self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                color = self.grid.colors[self.grid.grid[row][col]]
                rect = pygame.Rect(col * self.grid.size + 1, row * self.grid.size + 1, self.grid.size - 1, self.grid.size - 1)
                pygame.draw.rect(screen, color, rect)
        
        tiles = self.current_block.get_positions()
        for tile in tiles:
            rect = pygame.Rect(tile.col * self.current_block.size + 1,
                               tile.row * self.current_block.size + 1,
                               self.current_block.size - 1,
                               self.current_block.size - 1)
            pygame.draw.rect(screen, self.current_block.colors[self.current_block.id], rect)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.out_of_bounds() or self.collision():
            self.current_block.move(0, 1)
            return False
        return True

    def move_right(self):
        self.current_block.move(0, 1)
        if self.out_of_bounds() or self.collision():
            self.current_block.move(0, -1)
            return False
        return True
            
    def move_down(self):
        self.current_block.move(1, 0)
        if self.out_of_bounds() or self.collision():
            self.current_block.move(-1, 0)
            self.lock()
            return False
        return True
    
    def rotate(self,clockwise):
        self.current_block.rotate() if clockwise else self.current_block.unrotate()
        if self.out_of_bounds() or self.collision():
            self.current_block.unrotate() if clockwise else self.current_block.rotate()
            return False
        return True

    def collision(self):
        tiles = self.current_block.get_positions()
        for tile in tiles:
            if self.grid.is_occupied(tile.row, tile.col):
                return True
        return False

    def out_of_bounds(self):
        tiles = self.current_block.get_positions()
        for tile in tiles:
            if self.grid.out_of_bounds(tile.row, tile.col):
                return True
        return False
    
    def lock(self):
        tiles = self.current_block.get_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        lines = self.grid.check_rows()
        self.score += self.score_value[lines]
        if self.collision():
            self.game_over = True

    def get_features(self, grid):
        holes = 0
        heights = [0 for _ in range(10)]
        bump = 0
        row_is_full = [True for _ in range(20)]
        fulls = 0
        
        for col in range(10):
            ceiling = False
            for row in range(20):
                if grid[row][col] > 0:
                    if not ceiling:
                        ceiling = True
                        heights[col] = 20 - row
                else:
                    holes += int(ceiling)
                    row_is_full[row] = False
            if col > 0:
                bump += abs(heights[col] - heights[col - 1])

        for row in row_is_full:
            fulls += row
        
        return [holes, bump, fulls, max(heights)]

    def simulate(self):
        states = []
        actions = []
        game = copy.deepcopy(self)
        for state in range(len(game.current_block.cells)):
            for col in range(6): # move left
                grid = copy.deepcopy(game.grid.grid)
                while True:
                    game.current_block.move(1, 0)
                    if game.out_of_bounds() or game.collision():
                        game.current_block.move(-1, 0)
                        tiles = game.current_block.get_positions()
                        for position in tiles:
                            if position.row < 0:
                                continue
                            grid[position.row][position.col] = game.current_block.id
                        break
                if grid not in states:
                    states.append(grid)
                    actions.append((state, -col))

                game.current_block.row_offset = game.current_block.spawn_row
                if not game.move_left():
                    break
            game.current_block.col_offset = game.current_block.spawn_col
            for col in range(1, 6): # move right
                if not game.move_right():
                    break
                grid = copy.deepcopy(game.grid.grid)
                while True:
                    game.current_block.move(1, 0)
                    if game.out_of_bounds() or game.collision():
                        game.current_block.move(-1, 0)
                        tiles = game.current_block.get_positions()
                        for position in tiles:
                            if position.row < 0:
                                continue
                            grid[position.row][position.col] = game.current_block.id
                        break
                if grid not in states:
                    states.append(grid)
                    actions.append((state, col))
                game.current_block.row_offset = game.current_block.spawn_row
            game.current_block.col_offset = game.current_block.spawn_col
            if not game.rotate(0):
                break
        return (states, actions)