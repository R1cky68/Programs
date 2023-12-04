import pygame, sys, random, os

pygame.init()

os.environ["NSApplicationSupportSecureRestorableState"] = "1"

# Initial variables and setting up display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

black = (0,0,0)
red = (255, 0, 0)
white = (255,255,255)

# Snake properties
snake_size = 20
snake_speed = 15
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"

# Food generation
food = (random.randrange(1, (width//snake_size)) * snake_size, random.randrange(1, (height//snake_size)) * snake_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Registering controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"

            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    if abs(snake[0][0] - food[0]) < snake_size and abs(snake[0][1] - food[1]) < snake_size:
        food = (random.randrange(1, (width//snake_size)) * snake_size, random.randrange(1, (height//snake_size)) * snake_size)
        
    else: 
        snake.pop()

    # Moving snake
    if snake_direction == "UP":
        new_head = (snake[0][0], snake[0][1] - snake_size)

    elif snake_direction == "DOWN":
        new_head = (snake[0][0], snake[0][1] + snake_size)

    elif snake_direction == "LEFT":
        new_head = (snake[0][0] - snake_size, snake[0][1])

    elif snake_direction == "RIGHT":
        new_head = (snake[0][0] + snake_size, snake[0][1])

    # Collisions
    if (
        snake[0][0] >= width
        or snake[0][0] < 0
        or snake[0][1] >= height
        or snake[0][1] < 0
        or snake[0] in snake[1:]

    ):
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)
    
    # Drawing everything
    window.fill(black)

    # Not sure why 2 snake_size variables
    for segment in snake:
        pygame.draw.rect(window, white, (segment[0], segment[1], snake_size, snake_size))

    pygame.draw.rect(window, red, (food[0], food[1], snake_size, snake_size))

    pygame.display.flip()

    # Game speed
    pygame.time.Clock().tick(snake_speed)

    

