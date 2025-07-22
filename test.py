import pygame,pickle
from ai import NeuralNetwork
from game import Game
from colors import Colors
import numpy as np

def game_logic(net):
    GAME_UPDATE = pygame.USEREVENT
    game = Game()
    
    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return game.score
        states, actions = game.simulate()
        
        best_score = float('-inf')
        best_action = None

        scoreboard = font.render(str(game.score),True,Colors.white)

        game.draw(screen)
        screen.blit(scoreboard,(2,2))

        pygame.display.update()

        for grid, action in zip(states, actions):
            features = np.array(game.get_features(grid))
            score = net.forward(features)
            
            if score > best_score:
                best_score = score
                best_action = action
        
        if best_action:
            rotation, move = best_action
            for _ in range(rotation):
                game.rotate(0)
            if move < 0:
                for _ in range(abs(move)):
                    game.move_left()
            elif move > 0:
                for _ in range(move):
                    game.move_right()
            while True:
                if not game.move_down(): break
        else:
            break
        clock.tick(60)
    pygame.quit()
    return game.score

if __name__ == '__main__':
    with open("models/mynet3", 'rb') as f:
        net:NeuralNetwork = pickle.load(f)

    pygame.init()
    screen = pygame.display.set_mode((30*10,30*20))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,40)
    print(game_logic(net))