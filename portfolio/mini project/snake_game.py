import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display dimensions
width = 600
height = 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Create game window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, x, y):
    text = font.render(msg, True, color)
    win.blit(text, [x, y])

def gameLoop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    dx, dy = 0, 0

    snake = []
    length = 1

    food_x = random.randrange(0, width - snake_block, 10)
    food_y = random.randrange(0, height - snake_block, 10)

    while not game_over:
        while game_close:
            win.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", red, 50, height / 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        # Move the snake
        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        win.fill(blue)
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]
            

        for segment in snake[:-1]:
            if segment == [x, y]:
                game_close = True

        for segment in snake:
            pygame.draw.rect(win, white, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - snake_block, 10)
            food_y = random.randrange(0, height - snake_block, 10)
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
