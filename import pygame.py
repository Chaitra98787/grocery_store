import pygame
import time

pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) 


# Set the title of the game
pygame.display.set_caption("Car   Game")

# Load the car image
car_image = pygame.image.load("car.png")
car_x = (screen_width / 2) - (car_image.get_width() / 2)
car_y = (screen_height - car_image.get_height()) - 10

# Set the car's initial speed and direction
car_x_change = 0
car_y_change = 0

# Game loop
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

                car_x_change = -5
            elif event.key == pygame.K_RIGHT:
                car_x_change = 5
            elif event.key == pygame.K_UP:
                car_y_change = -5
            elif event.key == pygame.K_DOWN:
                car_y_change = 5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                car_y_change = 0

    car_x += car_x_change
    car_y += car_y_change

    # Check if the car is off the screen
    if car_x < 0 or car_x >= screen_width - car_image.get_width():
        car_x_change = 0
    if car_y < 0 or car_y >= screen_height - car_image.get_height():
        car_y_change = 0

    screen.fill((255, 255, 255))
    screen.blit(car_image, (car_x, car_y))
    pygame.display.update()

    # Add a delay to control the game speed
    time.sleep(0.05)

pygame.quit()
quit()