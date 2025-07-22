import pygame,sys
from game import Game

pygame.init()

screen = pygame.display.set_mode((30*10,30*20))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
font = pygame.font.Font(None,40)

GAME_UPDATE = pygame.USEREVENT
#pygame.time.set_timer(GAME_UPDATE,300)

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_UP:
                    game.rotate(0)
                if event.key == pygame.K_END:
                    game.rotate(1)
            if event.type == GAME_UPDATE:
                game.move_down()
        else:
            if event.type == pygame.KEYDOWN:game = Game()

    scoreboard = font.render(str(game.score),True,(255,255,255))

    game.draw(screen)
    screen.blit(scoreboard,(2,2))

    pygame.display.update()
    clock.tick(60)