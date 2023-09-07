import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 720, 1450
BALL_RADIUS = 50
BALL_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
FPS = 60
GRAVITY = 0.3  # Acceleration due to gravity

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball with Motion Effects")

# Ball properties
ball_x = WIDTH // 10
ball_y = HEIGHT // 10
ball_speed_x = 10
ball_speed_y = -10  # Initial upward velocity

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Apply gravity to the vertical speed
    ball_speed_y += GRAVITY

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with walls
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > WIDTH:
        ball_speed_x *= -1

    if ball_y - BALL_RADIUS < 0:
        ball_speed_y *= -1
        ball_y = BALL_RADIUS  # Prevent the ball from getting stuck at the top

    if ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y *= -0.8  # Bounce with reduced energy
        ball_y = HEIGHT - BALL_RADIUS  # Prevent the ball from going below the floor

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)
